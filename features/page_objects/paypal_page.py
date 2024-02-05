import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .base_page_object import BasePage


class PaypalCredentials:
    def __init__(self):
        self.paypal_details = \
            {
                "UK":
                    {
                        "email": "uk@tails.com",
                        "password": "Testing1234",
                    },
                "NI":
                    {
                        "email": "uk@tails.com",
                        "password": "Testing1234",
                    },
                "FR":
                    {
                        "email": "french@tails.com",
                        "password": "testing1234",
                    },
                "DE":
                    {
                        "email": "germany@tails.com",
                        "password": "testing1234",
                    },
                "NL":
                    {
                        "email": "netherlands@tails.com",
                        "password": "testing1234",
                    },
                "IE":
                    {
                        "email": "ireland@tails.com",
                        "password": "testing1234",
                    },
                "AT":
                    {
                        "email": "austria@tails.com",
                        "password": "testing1234",
                    },
                "BE":
                    {
                        "email": "belgium@tails.com",
                        "password": "testing1234",
                    },
                "DK":
                    {
                        "email": "denmark@tails.com",
                        "password": "testing1234",
                    },
                "SE":
                    {
                        "email": "sweden@tails.com",
                        "password": "testing1234",
                    },
                "PROD_UK":
                    {
                        "email": "qachamp@tails.com",
                        "password": "QAchamp4000!!",
                    },

            }


# This class is for paypal website functions and elements only
class PaypalPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def login_to_paypal(self, country):
        """ Completes the checkout process via PayPal. """
        # Wait for the new window or tab
        time.sleep(5)
        self.number_of_windows(2)
        time.sleep(15)
        # Do paypal actions
        paypal_login = PaypalCredentials()
        self.browser.switch_to.window(self.browser.window_handles[1])

        time.sleep(7)
        # self.warning_close_cookie()
        self.email.send_keys(paypal_login.paypal_details[country]["email"])
        self.paypal_next_button.click()
        self.password.send_keys(paypal_login.paypal_details[country]["password"])

        self.paypal_login_button.click()
        # Some paypal accounts have multiple cards linked to paypal and NI uses same account as UK
        if country not in ("UK", "BE", "IE", "FR", "SE", "DK", "NI", "DE", "PROD_UK"):
            self.paypal_choose_payment_method_continue_button.click()

            time.sleep(1)
            self.paypal_confirm_card_button.click()
        else:
            time.sleep(3)

            button = WebDriverWait(self.browser, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Agree & Continue']"))
            )
            button.click()

        self.browser.switch_to.window(self.browser.window_handles[0])

    def warning_close_cookie(self):
        time.sleep(5)
        try:
            if self.find('#acceptAllButton'):
                self.click_element_('#acceptAllButton')
        except NoSuchElementException:
            pass

    locator_dictionary = {
        "pricing_plan": (By.CSS_SELECTOR, "body.signup-price-summary"),
        "paypal_option": (By.CSS_SELECTOR, ".payment-options label[for=paypal-radio]"),
        "paypal_button": (By.ID, "paypal-button"),
        "email": (By.CSS_SELECTOR, "input#email"),
        "password": (By.CSS_SELECTOR, "input#password"),
        "paypal_login_button": (By.ID, "btnLogin"),
        "paypal_next_button": (By.CSS_SELECTOR, "button[type='submit']"),
        "paypal_confirm_card_button": (By.ID, "consentButton"),
        "paypal_choose_payment_method_continue_button": (By.ID, "fiSubmitButton"),
        "paypal_consent_button": (By.CSS_SELECTOR, "#consentButton"),
        "paypal_accept_cookie": (By.ID, "acceptAllButton"),

    }
