from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class IdealTestPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def mollie_status_button(self, status):
        return self.find_xpath(f"//*[@class='table-zebra table--select-status']//span[contains(text(),'{status}')]")

    locator_dictionary = {
        "yes_button": (By.CSS_SELECTOR, ".ideal-details label[for=delivery-address-yes]"),
        "no_button": (By.CSS_SELECTOR, ".ideal-details label[for=delivery-address-no]"),
        "continue_button": (By.XPATH, '//*[@class="btn redesign btn-primary btn-heavy ideal"]'),

        # Mollie test integration pages
        "ing_button": (By.XPATH, "//*[@id='body']//span/p[contains(text(),'ING')]"),
        "continue_button_mollie": (By.XPATH, '//*[@id="body"]/div[2]/div/button'),

    }
