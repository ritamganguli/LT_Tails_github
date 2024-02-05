from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class NewFoodPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {
        "feeding_preference_form": (By.CSS_SELECTOR, "#form_feeding-preference"),
        "feeding_pref_dry": (By.CSS_SELECTOR, "label[for=feeding_pref_dry]"),
        "feeding_pref_dry_wet": (By.CSS_SELECTOR, "label[for=feeding_pref_dry-wet]"),
        "feeding_pref_dry_wet_treats": (
            By.CSS_SELECTOR,
            "label[for=feeding_pref_dry-wet-treats]",
        ),
    }
