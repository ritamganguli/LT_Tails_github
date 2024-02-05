from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base_page_object import BasePage
import time


class PaymentPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    # placed the checkout code in this page to call from steps page
    def checkout_stripe_payment(self):
        time.sleep(15)
        card = ("4242424242424242",)
        expiry = ("1028",)
        cvc = "111"

        time.sleep(10)
        self.wait_for(
            ".step[data-step=your-payment-details][data-status=active] form",
            EC.presence_of_element_located,
        )

        card_errors = self.wait_for(".card-errors", EC.presence_of_element_located)

        with self.iframe("#card-number iframe"):
            self.input_text("input[name=cardnumber]", card, typing_delay=0.2)
        time.sleep(1)
        self.click_element_(".btn.btn-primary.icon-lock")
        time.sleep(1)
        assert (
                card_errors.text == "Your card's expiration date is incomplete."
                or card_errors.text != ""
        )  # for translations

        with self.iframe("#card-expiry iframe"):
            self.input_text("input[name=exp-date]", expiry, typing_delay=0.2)

        self.click_element_(".btn.btn-primary.icon-lock")
        time.sleep(1)
        assert (
                card_errors.text == "Your card's security code is incomplete."
                or card_errors.text != ""
        )  # for translations

        with self.iframe("#card-cvc iframe"):
            self.input_text("input[name=cvc]", cvc, typing_delay=0.2)

        time.sleep(5)
        self.click_element_(
            ".btn.btn-primary.icon-lock"

        )

    # this only used for pipeline tests - builds on staging
    def checkout_stripe_payment_not_checking_error(self):
        time.sleep(10)
        card = ("4242424242424242",)
        expiry = ("1028",)
        cvc = "111"

        time.sleep(10)
        self.wait_for(
            ".step[data-step=your-payment-details][data-status=active] form",
            EC.presence_of_element_located,
        )

        with self.iframe("#card-number iframe"):
            self.input_text("input[name=cardnumber]", card, typing_delay=0.2)
        time.sleep(1)

        with self.iframe("#card-expiry iframe"):
            self.input_text("input[name=exp-date]", expiry, typing_delay=0.2)

        with self.iframe("#card-cvc iframe"):
            self.input_text("input[name=cvc]", cvc, typing_delay=0.2)

        time.sleep(5)
        self.click_element_(
            ".btn.btn-primary.icon-lock"
        )

        # this only used for test signup on Production (caution this will create real payment - Mario B pleo card
        # details)
    def checkout_stripe_payment_not_checking_error_for_prod(self):
        time.sleep(10)
        prod_card = ("5191590000328961",)
        prod_expiry = ("0425",)
        prod_cvc = "091"

        self.wait_for(
            ".step[data-step=your-payment-details][data-status=active] form",
            EC.presence_of_element_located,
        )

        with self.iframe("#card-number iframe"):
            self.input_text("input[name=cardnumber]", prod_card, typing_delay=0.2)
        time.sleep(1)

        with self.iframe("#card-expiry iframe"):
            self.input_text("input[name=exp-date]", prod_expiry, typing_delay=0.2)

        with self.iframe("#card-cvc iframe"):
            self.input_text("input[name=cvc]", prod_cvc, typing_delay=0.2)

        time.sleep(5)
        self.click_element_(
            ".btn.btn-primary.icon-lock"

        )

    def checkout_openbanking(self):
        # This timeout is needed to be less than Base page's 70s
        # because it impacts the time it takes for the t&c checkbox to be selected
        self.timeout = 50
        self.given_name.send_keys("name")
        self.family_name.send_keys("family")
        self.email.send_keys("openbanking@tails.com")
        self.address_line1.send_keys("Alt-Moabit 3")
        self.city.send_keys("Oschatz")
        self.postal_code.send_keys("04752")
        self.continue_button.click()
        self.iban.send_keys("DE89370400440532013000")
        self.second_continue_button.click()
        self.authorise_success_payment.click()
        self.browser.execute_script("arguments[0].click();", self.t_and_c)
        self.submit.click()
        time.sleep(10)
        self.next.click()
        time.sleep(10)

    locator_dictionary = {
        "local_details": (By.CSS_SELECTOR, "label[for=local-details-toggle]"),
        "account_number": (By.CSS_SELECTOR, "#account_number"),
        "bank_code": (By.CSS_SELECTOR, "#bank_code"),
        "submit_bank": (By.XPATH, "//*[@id='gocardless-form']//button[contains(text(),'Zur Bestätigung und "
                                  "Unterschrift')]"),
        "submit_order": (By.XPATH, "//*[@id='gocardless-form']//button[contains(text(),'Kostenpflichtig bestellen')]"),

        # Open Banking Locators
        "given_name": (By.ID, "given_name"),
        "family_name": (By.ID, "family_name"),
        "email": (By.ID, "email"),
        "address_line1": (By.ID, "address_line1"),
        "city": (By.ID, "city"),
        "postal_code": (By.ID, "postal_code"),
        "continue_button": (By.XPATH, "//span[normalize-space()='Continue']"),
        "iban": (By.ID, "iban"),
        "second_continue_button": (By.CSS_SELECTOR, "button[type='submit']"),
        "authorise_success_payment": (By.XPATH, "//span[@class='css-rg4oaw'][normalize-space()='Success Bank - "
                                                "Automatically authorises the payment request']"),
        "t_and_c": (By.ID, 'gc-eu-terms-and-conditions'),
        "submit": (By.XPATH, "//button[@type='submit']"),
        "chrome": (By.XPATH, "//span[normalize-space()='Continue on chrome']"),
        "next": (By.XPATH, '//*[@id="__next"]/div/div/div/div[1]/div/div[3]/div/a'),
        "header": (By.XPATH, "//h1[normalize-space()='Vielen Dank']"),
    }
