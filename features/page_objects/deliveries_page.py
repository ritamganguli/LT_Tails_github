import sys
import time
import datetime
import platform
from dateutil.relativedelta import relativedelta

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class DeliveriesPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def check_delivery_date_range(self, actual_next_delivery_window, expected_next_delivery_range):
        found = False

        for thisDate in expected_next_delivery_range:
            print("Delivery window displayed: " + actual_next_delivery_window, file=sys.stderr)
            print("Checking: " + thisDate, file=sys.stderr)
            found = thisDate in actual_next_delivery_window
            if found:
                break
            else:
                continue
        return found

    def check_new_delivery_date(self, new_date):
        try:
            self.find_xpath(f"//*[contains(text(),'{new_date}')]")
            print("Date matched", file=sys.stderr)
            return True
        except NoSuchElementException:
            print("Date not matched", file=sys.stderr)
            return False

    # Transform date into a format like Wed, 9 February 2022
    # strftime uses either dash(-) for Linux and MAC, ect or hash(#) for Windows
    # https://strftime.org/
    @staticmethod
    def paused_deliveries_notification_date_format():
        return '%#d %B' if platform.system() == 'Windows' else '%-d %B'

    def delayed_delivery_month(self, num_month, date_reference):
        """method to calculate the next delivery month based user selection on how many month(s) to delay"""

        delayed_delivery_date1 = date_reference + relativedelta(months=+num_month)
        delayed_delivery_date2 = date_reference + relativedelta(months=+num_month, days=-1)
        delayed_delivery_date3 = date_reference + relativedelta(months=+num_month, days=-2)
        delayed_delivery_date4 = date_reference + relativedelta(months=+num_month, days=+1)
        delayed_delivery_date5 = date_reference + relativedelta(months=+num_month, days=+2)
        # Convert to Y-m-d format
        delayed_delivery_date1 = delayed_delivery_date1.strftime(self.paused_deliveries_notification_date_format())
        delayed_delivery_date2 = delayed_delivery_date2.strftime(self.paused_deliveries_notification_date_format())
        delayed_delivery_date3 = delayed_delivery_date3.strftime(self.paused_deliveries_notification_date_format())
        delayed_delivery_date4 = delayed_delivery_date4.strftime(self.paused_deliveries_notification_date_format())
        delayed_delivery_date5 = delayed_delivery_date5.strftime(self.paused_deliveries_notification_date_format())
        delayed_delivery_date = [delayed_delivery_date1, delayed_delivery_date2, delayed_delivery_date3,
                                 delayed_delivery_date4, delayed_delivery_date5]
        print(delayed_delivery_date, file=sys.stderr)
        return delayed_delivery_date

    def delayed_delivery_two_weeks(self, date_reference, expected_days_range):
        """Generate a range of expected delayed deliveries for the next two weeks"""
        """Increase range of expected dates due to bank holiday weekends"""

        delayed_delivery_dates = [date_reference + relativedelta(days=+num_days)
                                  for num_days in expected_days_range]

        # Convert to Y-m-d format
        return [delayed_delivery_date.strftime(self.paused_deliveries_notification_date_format())
                for delayed_delivery_date in delayed_delivery_dates]

    # Convert dates with different formats like 31 December to this date 31 Dec
    # Link to different date format codes that can be used: https://strftime.org/
    @staticmethod
    def convert_date_to_delivery_due_date_format(date, date_format):
        new_date_format = "%#d %b" if platform.system() == 'Windows' else "%-d %b"
        print(str(date).strip(), file=sys.stderr)
        return datetime.datetime.strptime(str(date).strip(), date_format).strftime(new_date_format)

    # For context, this is applicable for page with deliveries/future/20220608/change-date in the URL
    @staticmethod
    def latest_delivery_day_month(new_date):
        """method to change the format of the new selected delivery date and extraxt the last expected [day] [month]
        from pets/petid/change-deliveries/ url"""
        "ie: extract '22 August' from 'Thursday, 19 August 2021 - Sunday, 22 August 2021'"
        return new_date.strip().split("-")[1].split(",")[1].split("202")[0].lstrip()

    # For context, this is applicable for page with /change-deliveries/ in the URL
    @staticmethod
    def latest_delivery_day_month_from_change_deliveries_move(new_date):
        """method to change the format of the new selected delivery date and extraxt the last expected [day] [month]
        from change-deliveries/move url"""
        "ie: extract '21 Aug' from 'Thu 19 Aug - Sat 21 Aug'"
        return (
                new_date.strip().split("-")[1].lstrip().split(" ")[1]
                + " "
                + new_date.strip().split("-")[1].lstrip().split(" ")[2]
        )

    def warning_close_cookie(self):
        time.sleep(0.3)
        try:
            if self.find('#cookie_prompt a[href="#"]'):
                self.click_element_('#cookie_prompt a[href="#"]')
        except NoSuchElementException:
            pass

    locator_dictionary = {
        "deliveries_header": (By.XPATH, "//*[@class='headline-main left']"),
        "view_delivery_button": (
            By.XPATH, "//*[@class='btn btn-primary'][contains(text(),'View full delivery details')]"),
        "next_delivery_header": (
            By.XPATH,
            "//*[@class='tails-view tails-view-shipment-details ']/h1",
        ),
        "notification": (By.CSS_SELECTOR, "#notifications"),
        "delivery_details": (
            By.XPATH,
            "//a[normalize-space()='View full delivery details']",
        ),
        "delivery_details_header": (
            By.XPATH,
            "//h1[normalize-space()='Next delivery']",
        ),
        "manage_my_box_page_pet_header": (
            By.CSS_SELECTOR,
            ".pet-name-title",
        ),
        "box_breakdown_component": (
            By.CSS_SELECTOR,
            ".boxbreakdown-main",
        ),
        "manage_my_box_dry_food_item": (By.CSS_SELECTOR, ".boxbreakdown-item:nth-child(1) .item-details-container h3"),
        "manage_my_box_button": (
            By.CSS_SELECTOR,
            "div.tails-view.tails-view-current-shipments.tails-shipments > div.shipment > div > .btn.btn-primary",
        ),
        "change_delivery_date_link": (
            By.CSS_SELECTOR,
            ".change-delivery-date a",
        ),
        "change_delivery_header": (
            By.XPATH,
            "//h1[normalize-space()='Change delivery date']",
        ),
        "change_delivery_date_reason": (By.XPATH, "//p[normalize-space()='Please let us know the reason you are "
                                                  "changing the date of this delivery.'] "),
        "new_delivery_date": (By.XPATH, "//select[@id='new-delivery-date']"),
        "new_delivery_date_option": (By.XPATH, "//*[@id='new-delivery-date']/option[9]"),
        "submit_change_date": (By.XPATH, "//*[@type='submit'][@class='btn btn-primary']"),
        "submit_reason": (By.XPATH, "//*[@type='submit'][@class='btn btn-primary']"),
        "change_date_confirmation": (By.XPATH, "//*[@class='heading-and-dismiss']"),

        "delay_delivery_one_month": (By.XPATH, "//label/span[contains(text(),'1 Month')]"),
        "delay_delivery_two_month": (By.XPATH, "//label/span[contains(text(),'2 Month')]"),
        "delay_delivery_two_weeks": (By.XPATH, "//label/span[contains(text(),'2 Weeks')]"),
        "confirm_pause_delivery": (By.XPATH, "//button[normalize-space()='Save and continue']"),
        "pause_delivery_confirmation": (By.CSS_SELECTOR, ".content-card.next-delivery > p"),
        "delay_confirmation_new_delivery_date": (By.CSS_SELECTOR, ".date"),
        "delivery_due_date": (By.ID, "delivery-due-date"),
        "Sent_in_next_box_notification": (By.CSS_SELECTOR, "div.one-off-notification"),
        "fwt_delivery_header": (By.XPATH, "//h3[normalize-space()='Monthly flea, tick & worm treatment']"),
        "view_treatment_delivery_button": (By.XPATH, "//*[@id='tails-view-3']/div[2]/div/a"),
        "confirm_fwt_next_delivery": (By.XPATH, "//*[@id='tails-view-3']/div/table/tbody/tr[1]/td[1]/div/p"),
        "delivery_breakdown": (By.XPATH, "//*[@class='boxbreakdown-main']"),
        "old_ui_breakdown": (By.XPATH, "//*[@class='content']"),
        "change_delivery_date_button": (By.XPATH, "//*/button[contains(text(),'change delivery date')]"),
    }
