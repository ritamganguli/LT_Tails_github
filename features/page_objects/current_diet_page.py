from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class CurrentDietPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {
        "current_diet_form": (By.CSS_SELECTOR, "#form_current-diet"),
        "current_dryfood": (By.CSS_SELECTOR, "label[for=current-dry-food]"),
        "current_drywet": (By.CSS_SELECTOR, "label[for=current-wet-food]"),
        "current_otherfood": (By.CSS_SELECTOR, "label[for=current-other-food]"),
        "diet_next": (By.XPATH, '//*[@id="form_current-diet"]/div[2]/div/button')
    }
