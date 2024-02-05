from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class BreedPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {
        "breed_form": (By.CSS_SELECTOR, "#form_breed"),
        "purebreed_input": (By.CSS_SELECTOR, "label[for=breed-type-choice-purebreed]"),
        "crossbreed_input": (
            By.CSS_SELECTOR,
            "label[for=breed-type-choice-crossbreed]",
        ),
        "unknown_breed": (By.CSS_SELECTOR, "#breed-type-label-unknown"),
        "breed_search": (By.CSS_SELECTOR, 'input[name="breed-selector-0"]'),
        "crossbreed_search": (By.CSS_SELECTOR, 'input[name="breed-selector-4"]'),
        "breed_search_second": (By.CSS_SELECTOR, 'input[name="breed-selector-1"]'),
        "second_breed_select": (By.XPATH, "//*[@name='breed-selector-1']"),
        "breed_search_third": (By.CSS_SELECTOR, 'input[name="breed-selector-2"]'),
        "third_breed_select": (By.XPATH, "//*[@name='breed-selector-2']"),
        }
