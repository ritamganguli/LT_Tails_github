from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class UpdatePortionPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {

        "enter_amount": (By.CSS_SELECTOR, ".info .btn.btn-primary"),
        "input_grams_link": (By.ID, "input-grams-link"),
        "next_button": (By.ID, "next_btn"),
        "dashboard": (By.XPATH, "//div[contains(@class,'navigation-content')]//span[@class='text'][normalize-space("
                                ")='Dashboard']"),
        "enter_grams": (By.ID, "wet_grams"),

    }
