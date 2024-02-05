from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class MotivationPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {
        "motivation_form": (By.CSS_SELECTOR, "#form_motivation"),
        "gain_weight": (By.CSS_SELECTOR, "label[for=motivation-1]"),
        "motivation_info_form": (By.CSS_SELECTOR, "#form_weight-motivation-info"),
        "motivation_back": (By.XPATH, "//*[@id='form_motivation']/div[2]/div/a/span"),
    }
