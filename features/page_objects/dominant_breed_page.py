from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class DominantPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def dominant_breed_first(self, firstbreed):
        return self.find_xpath(f"//*[@id='form_dominant']//span[contains(text(),'{firstbreed}')]")

    def dominant_breed_second(self, secondbreed):
        return self.find_xpath(f"//*[@id='form_dominant']//span[contains(text(),'{secondbreed}')]")

    def dominant_breed_third(self, thirdbreed):
        return self.find_xpath(f"//*[@id='form_dominant']//span[contains(text(),'{thirdbreed}')]")

    locator_dictionary = {
        "dominant_form": (By.CSS_SELECTOR, "#form_dominant"),

        "first_dominant_breed": (
            By.XPATH, "//*[@id='form_dominant']//span[contains(text(),'Cockapoo')]"),
        "second_dominant_breed": (
            By.CSS_SELECTOR, "label[for=dominant_breed-choice-1]"),
        "third_dominant_breed": (
            By.CSS_SELECTOR, "label[for=dominant_breed-choice-2]"),
        "unknown_dominant_breed": (
            By.CSS_SELECTOR, "lable[for=dominant_breed-choice-10]"),
        "dominant_back": (By.XPATH, "//*[@id='form_dominant']/div[2]/div/a/span"),

    }
