from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class WeightConfirmPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {

        "weight_confirm": (By.XPATH, "//*[@class='btn btn-primary']")
    }