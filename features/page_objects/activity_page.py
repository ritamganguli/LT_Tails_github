from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
)
from .base_page_object import BasePage


class ActivityPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def puppy_route(self, timeout=15):
        wait = WebDriverWait(self.browser, timeout)
        try:
            # Try to wait for the primary element to become present and then return it
            return wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#form_activity")))
        except TimeoutException:
            # If waiting for the primary element fails, pass to next step
            pass

    locator_dictionary = {
        "": (By.CSS_SELECTOR, ""),
        "activity_form": (By.CSS_SELECTOR, "#form_activity"),
    }
