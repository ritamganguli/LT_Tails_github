from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class WeightPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {
        "weight_form": (By.CSS_SELECTOR, "#form_weight"),
        "weight_input": (By.CSS_SELECTOR, "input[name=weight-kg]"),
        "gain_a_lot_of_weight": (By.CSS_SELECTOR, "label[for=condition-4020367548]"),
        "maintain_weight": (By.CSS_SELECTOR, "label[for=condition-ideal]"),
        "gain_little_weight": (By.CSS_SELECTOR, "label[for=condition-underweight"),
        "underweight_info_form": (By.CSS_SELECTOR, "#form_underweight-info"),
        "estimate_weight_link": (By.CSS_SELECTOR, "#weight-help-label"),
        "estimate_weight_button": (By.CSS_SELECTOR, "#weight-estimate-button"),
        "weight_error_notification": (By.XPATH, "//*[@class='notifications']"),
    }
