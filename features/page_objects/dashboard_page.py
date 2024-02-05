import time

from selenium.webdriver.common.by import By
from .base_page_object import BasePage
from selenium.common.exceptions import NoSuchElementException


class DashboardPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def secret_mission_dismiss(self):
        if self.secret_mission_close.is_displayed():
            self.secret_mission_close.click()
        else:
            pass

    def dashboard_feed_survey_dismiss(self):
        # Always wait as survey pop up is not always instant
        time.sleep(15)
        try:
            # Using the locator dictionary is too slow as timeout always kicks in, hence using default selenium code
            self.find_xpath_not_dictionary("//*/body/div[6]/div/div/button").is_displayed()
            self.find_xpath_not_dictionary("//*/body/div[6]/div/div/button").click()

        except NoSuchElementException:
            pass

    def dashboard_feed_better_service_dismiss(self):
        # Always wait as survey pop up is not always instant
        time.sleep(15)
        try:
            # Using the locator dictionary is too slow as timeout always kicks in, hence using default selenium code
            self.find_xpath_not_dictionary("//*/div[5]/div/div/button").is_displayed()
            self.find_xpath_not_dictionary("//*/div[5]/div/div/button").click()

        except NoSuchElementException:
            pass

    def survey_close_cookie(self):
        time.sleep(20)
        try:
            element_one = self.survey_close
            element_one.click()
        except NoSuchElementException:
            pass

    # "Page animation occurs every time you load dashboard can block clicking elements during a test"
    def wait_for_new_account_loading_animation_to_disappear(self):
        self.wait_for_element_to_be_invisible(self.new_account_loading_page_animation, 30)

    locator_dictionary = {
        "continue_dashboard": (By.LINK_TEXT, "Continue to my dashboard"),
        "fr_continue_dashboard": (By.LINK_TEXT, "Continuer vers mon tableau de bord"),
        "de_continue_dashboard": (By.LINK_TEXT, "Weiter zu meinem Dashboard"),
        "nl_continue_dashboard": (By.LINK_TEXT, "Ga verder naar mijn dashboard"),
        "new_account_loading_page_animation": (By.ID, "graceful-mounting-element"),
        # Hamburger menu links
        # "hamburger_menu": (By.XPATH, "//*/label/span[2][contains(text(),'Menu')]"),
        "hamburger_menu": (By.CSS_SELECTOR, "label[for=hamburger]"),
        "account_page_select": (By.XPATH, "//*[@class='side-nav']//*[@data-selenium='account']"),
        "profile_page_select": (By.XPATH, "//*[@class='side-nav']//*[@data-selenium='profile']"),
        "shop_page_select": (By.XPATH, "//*[@class='side-nav']//*[@data-selenium='shop']"),
        "deliveries_page_select": (By.XPATH, "//*[@class='side-nav']//*[@data-selenium='deliveries']"),
        "raf_page_select": (By.XPATH, "//*[@class='side-nav']//*[@data-selenium='raf']"),
        "dashboard_page_select": (By.XPATH, "//*[@class='side-nav']//*[@data-selenium='dashboard']"),
        "treatment_page": (By.XPATH, "//*[@class='side-nav']//*[@data-selenium='treatment']"),

        "feeding_plan_page_select": (By.XPATH, "//*[@class='side-nav']//*[@data-selenium='feeding-plan']"),
        "tutorial_space_close": (
            By.XPATH,
            "//*[@class='getting-started-container tutorial-space-v2']//div/a/button[contains(text(),"
            "'Go to dashboard')]",
        ),
        "cancel_quick_link": (By.XPATH, "//*[contains(@href,'/cancel')]"),
        "feed_survey_close": (By.XPATH, "//*/body/div[6]/div/div/button"),
        "cancel_quick_link_FR": (By.XPATH, "//*/button[contains(text(),'Annuler')]"),
        "cancel_quick_link_DE": (By.XPATH, "//*/button[contains(text(),'Abo beenden ')]"),
        "restart_cancelled_subscription_button": (By.XPATH, "//*[@data-testid='subscription-reactivation']"),
        "resume_paused_subscription_button": (By.XPATH, "//*[@data-testid='subscription-reactivation']"),
        "next_button": (By.XPATH, "//*[@class='btn btn-primary next']"),
        "next_button_reactivate": (By.XPATH, "//*[@id='reactivation-next-button']"),
        "restart_confirm": (By.CSS_SELECTOR, ".reactivation-buttons button"),
        "delivery_header": (
            By.XPATH, "//*[contains(text(),' Scheduled Deliveries ')]"),
        "delivery_header_cancelled": (
            By.CSS_SELECTOR, ".reactivation-details .delivery > div:nth-child(2)"),
        # "change_delivery_date_component": (
        #     By.XPATH,
        #     "//*[@class='delivery-details-btn'][@data-heap='nd-change-delivery-date']",
        # ),

        # Quick links section
        "delay_or_pause": (By.XPATH, "//*[contains(text(), 'Pause/delay deliveries')]"),
        "confirm_button": (By.XPATH, "//*[@class='btn btn-primary']"),
        "pause_deliveries": (By.XPATH, "//a[contains(@href,'/choose-pause')]"),
        "pause_indefinitely": (
            By.XPATH,
            "//*[@for='manual']/span[contains(text(),'Until I Restart')]",
        ),
        "pause_reason": (By.CSS_SELECTOR, "label[for='reason_3'] span[class='text']"),
        "pause_reason_other": (By.XPATH, "//label[@for='reason_22']"),
        "other_reason_explanation": (By.XPATH, "//input[@id='more_details_22']"),
        "paused_delivery_header": (By.XPATH, "//*/div/div/div[4]/p[contains(text(),'deliveries are paused')]"),
        "change_delivery_quick": (By.XPATH, "//*/button[contains(text(),'Pause/delay deliveries')]"),
        "date_dropdown": (By.XPATH, "//select[@id='delivery_date']"),
        "new_delivery_date_option": (By.XPATH, "//*[@id='delivery_date']/option[2]"),
        "reason_change": (By.CSS_SELECTOR, "label[for='reason_1']"),
        "confirm_reason": (By.XPATH, "//*[@class='buttons-wrapper-aligned']/button[@class='btn btn-primary']"),
        "notification": (By.CSS_SELECTOR, "#notifications"),
        "add_dog_quick_link": (By.XPATH, "//*/button[contains(text(),'Add a new dog ')]"),
        "new_dog_name": (By.XPATH, "//*[@name='new_pets_name']"),
        "start_profile_button": (By.CSS_SELECTOR, "#add-dog>form>button"),
        "my_dog_header": (By.XPATH, "//*[@class='step-header']"),
        "log_out": (By.XPATH, "//*[@class='link signout with-icon ']"),
        "logged_out": (By.CSS_SELECTOR, "div[class='container clearfix'] p"),
        "dashboard_header": (By.XPATH, "//h1[@class='name']/span"),
        "wet_food_add_button": (By.CSS_SELECTOR, "div[class='logo'] a"),
        "wet_food_edit_button": (By.CSS_SELECTOR, "#wetfood"),
        "wet_food_edit_selection_button": (By.CSS_SELECTOR, "a[href='/gb/pets/916033478/wet-food-selection']"),
        "wet_food_tray_size": (By.CSS_SELECTOR, "#tray-size-150"),
        "Switch_to_150_g_trays": (By.XPATH, "//label[normalize-space()='Switch to 150g trays']"),
        "header_pet_name": (
            By.XPATH,
            "//*[@class='pet-details']/div[2]/h3[contains(text(),'Qa Champ')]",
        ),
        "quick_links_header": (By.XPATH, "//*[@class='section quick-links']//h3"),
        "secret_mission_close": (By.XPATH, "//*[@id='Page-1']"),
        "change_delivery_date_button": (By.XPATH, "//*[@class='change-date']/div/button[@class='btn btn-primary']"),
        "survey_close": (By.XPATH, "//button[contains(text(),'No thanks')]"),
        "pause_reason_price_tile": (By.XPATH, "//a[contains(@href, '/price')]"),
        "pause_deliveries_button": (By.CSS_SELECTOR, "button[type='submit']"),
        "order_extra_wet_food": (By.XPATH, "//*[@class='feeding-plan-lower view-feeding-btn btn-right']"),
        "wftu_card": (By.XPATH, "//*[@data-testid='wftu-card']"),
        "wet_food_header": (By.XPATH, "//*[@data-testid='order-type-wet']"),
        "add_wet_food_link": (By.CSS_SELECTOR, ".feeding-links a"),
        # the manage_box_cta element is nested, problematic to set a stable element locator - reverted to long path instead needs better
        # identifier
        "manage_box_cta": (By.XPATH, "//*[@id='app']/div/div/div/div/div[5]/div/div/div/div/div[2]/div[4]/button[contains(text(),'View & manage')]"),
        "view_full_deliveries_button": (By.XPATH, "//*[@class='btn btn-primary'][contains(text(),'View full delivery "
                                                  "details')]"),
        "edit_selection": (By.XPATH, "//div[@class='edit-and-remove mobile-only']//a[contains(text(),'Edit selection')]"),
        "update_wet_food": (By.XPATH, "//a[contains(text(),'Update flavours & textures')]")

    }
