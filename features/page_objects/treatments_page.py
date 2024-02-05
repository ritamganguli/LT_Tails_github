from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class TreatmentPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {

        "fwt_subscribe": (By.XPATH, "//button[@type='submit']"),
        "fwt_subscription_confirmation": (By.XPATH, "//*[@class='notification-content ']/p"),
        "fwt_unsubscribe": (By.XPATH, "//button[@value='unsubscribe']"),
        "fwt_unsubscription_confirmation": (By.XPATH, "//*[@class='notification-content ']/p")
    }
