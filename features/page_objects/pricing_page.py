import time

from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class PricingPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def select_paypal_payment_method(self, checkout_):
        self.paypal_payment_option.click()
        # PayPal button takes a while to fully display after selecting payment method but Selenium thinks it's ready
        time.sleep(10)
        # I noticed the screen just hangs if we don't scroll into the element
        if checkout_ == "checkout_english":
            # self.uk_paypal_checkout_button.click()
            self.browser.execute_script("arguments[0].scrollIntoView();", self.paypal_button)
            with self.iframe("#paypal-button > div > div > iframe"):
                # This was a last resort, selenium clicks did not work
                self.browser.execute_script("arguments[0].click();", self.uk_paypal_checkout_button)
        if checkout_ == "checkout_de":
            self.browser.execute_script("arguments[0].scrollIntoView();", self.paypal_button)
            with self.iframe("#paypal-button > div > div > iframe"):
                # This was a last resort, selenium clicks did not work
                self.browser.execute_script("arguments[0].click();", self.de_paypal_checkout_button)
        if checkout_ == "checkout_fr":
            self.browser.execute_script("arguments[0].scrollIntoView();", self.paypal_button)
            with self.iframe("#paypal-button > div > div > iframe"):
                # This was a last resort, selenium clicks did not work
                self.browser.execute_script("arguments[0].click();", self.fr_paypal_checkout_button)
        if checkout_ == "checkout_nl":
            self.browser.execute_script("arguments[0].scrollIntoView();", self.paypal_button)
            with self.iframe("#paypal-button > div > div > iframe"):
                # This was a last resort, selenium clicks did not work
                self.browser.execute_script("arguments[0].click();", self.nl_paypal_checkout_button)

    def pricing_payment_option_ideal(self):
        elements = self.browser.find_elements(By.XPATH, "//input[@name='provider']")
        print(len(elements))
        for _ in range(len(elements)):
            self.browser.find_elements(By.XPATH, "//input[@name='provider']")[2].click()

    def pricing_page_ideal_submit(self):
        locator = (By.XPATH, "//*[@id='submit-pricing-details']")
        # Find all elements matching the locator
        elements = self.browser.find_elements(*locator)
        # Check if any elements were found
        if elements:
            # Select the first instance of the element
            first_element = elements[0]
            first_element.click()
            print(first_element.text)
        else:
            print("No submit-pricing-details found")

    locator_dictionary = {
        "gocardlesscard_option": (By.CSS_SELECTOR, "label[for=gocardless-radio]"),
        "submit_gocardless": (
            By.XPATH, "//*[@id='submit-pricing-details']//span[contains(text(),'Weiter mit Lastschrift')]"),
        "dental_trial_pricing_page": (
            By.XPATH, "//*[@class='first trial price-table']//div[contains(text(),'Dental dailies')]"),
        "trial_pricing_table": (By.XPATH, "//*[@class='first trial price-table']"),
        "card_option": (By.CSS_SELECTOR, ".payment-options label[for=card-radio]"),
        "submit_pricing": (By.CSS_SELECTOR, "#submit-pricing-details"),
        "fr_submit_pricing": (By.XPATH, '//*[@id="submit-pricing-details"]/span'),
        "nl_submit_pricing": (By.CSS_SELECTOR, "#submit-pricing-details"),
        "de_submit_pricing": (
            By.XPATH,
            '//*[@id="submit-pricing-details"]/'
            'span[contains(text(),"Weiter mit Kartenzahlung")]',
        ),
        "yakers": (By.XPATH, "//*[text()='Yaker treats']"),

        "two_dogs": (
            By.XPATH,
            "//span[@class='sessioncamhidetext'][contains(text(),'Dogone and Dogtwo')]",
        ),
        "manage_dogs": (By.XPATH, "//*[@id='manage-dogs-profiles']"),
        "manage_dog": (By.XPATH, "//*/div[5]/div[2]/a[2]/span[contains(text(),'dog')]"),
        "de_manage_dog": (By.XPATH, "//*[@id='tails-view-7']/div[5]/div[2]/a/span"),
        "manage_dog_from_pricing": (
            By.XPATH,
            "//*/span[contains(text(),'dog')]",
        ),
        "another_dog": (By.XPATH, "//*[@data-ga-label='add-more']"),
        "submit_treats_page_nl": (
            By.XPATH, "//button[@class='button submit primary'][contains(text(),'Controleer je doos')]"),
        "ideal_option": (By.XPATH, "//*[@id='tails-view-2']/div[2]/fieldset/label[3]/div/div"),
        "standard_pricing_tab": (By.XPATH, "//*[@id='tails-view-1']/div[1]/div[3]/div[4]/label[2]"),
        "submit_pricing_ideal": (By.XPATH, "//*[@id='submit-pricing-details']/span"),
        "paypal_payment_option": (By.CSS_SELECTOR, ".payment-options label[for=paypal-radio]"),
        "paypal_button": (By.ID, "paypal-button"),
        "uk_paypal_checkout_button": (By.XPATH, "//span[@class='paypal-button-text'][contains(text(),' Checkout')]"),
        "de_paypal_checkout_button": (By.XPATH, "//span[@class='paypal-button-text'][contains(text(),'Direkt zu ')]"),
        "fr_paypal_checkout_button": (By.XPATH, "//span[@class='paypal-button-text'][contains(text(),' Payer')]"),
        "nl_paypal_checkout_button": (By.XPATH, "//span[@class='paypal-button-text'][contains(text(),' Betalen')]"),
        "price_table": (By.XPATH, "//*[@class='first trial price-table']"),
    }
