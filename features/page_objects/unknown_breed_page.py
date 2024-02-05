from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class UnknownBreedPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def select_unknown(self, unknown_breed_):
        return self.find_xpath(f"//*[@id='form_unknown']//span[contains(text(),'{unknown_breed_}')]").click()

    locator_dictionary = {
        "unknown_breed_form": (By.CSS_SELECTOR, "#form_unknown"),
        "unknown_breed_giant_uk": (By.XPATH, "//*[@id='form_unknown']//span[contains(text(),'Giant (over 40kg)')]"),
        "unknown_breed_giant_nl": (By.XPATH, "//*[@id='form_unknown']//span[contains(text(),'reus (40+ kg)')]"),
        "unknown_breed_giant_at": (By.XPATH, "//*[@id='form_unknown']//span[contains(text(),'Riese (über 40 kg)')]"),
    }
