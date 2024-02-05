from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class CurrentFoodPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {
        "current_food_form": (By.CSS_SELECTOR, "#form_current-food"),
        "no_dryfood_brand": (By.CSS_SELECTOR, "label[for=dry_food-no_brand]"),
        "flavours_form": (By.CSS_SELECTOR, "#form_flavours"),
        "flavours_form_next": (
            By.XPATH,
            '//*[@id="form_flavours"]/div[2]/div/button/span',
        ),
        "flavours_anything": (By.CSS_SELECTOR, "label[for=flavour-0]"),
        "flavours_fish": (By.CSS_SELECTOR, "#fish_flavour"),
        "flavours_lamb": (By.CSS_SELECTOR, "#lamb_flavour"),
        "current_wet": (By.XPATH, '//*[@id="format"]/optgroup[2]/option[1]'),
        "current_dry": (By.CSS_SELECTOR, '.brand-selector input'),
        "current_wet_france": (By.XPATH, '//*[@id="format"]/optgroup[3]/option[1]'),
        "current_wet_germany": (By.XPATH, '//*[@id="format"]/optgroup[3]/option[1]'),
        "textures_form": (By.CSS_SELECTOR, "#form_textures"),
        "feedpref_form": (By.CSS_SELECTOR, "#form_feeding-preference"),
        "large_wet_portion": (By.XPATH, '//*[@id="format"]/optgroup[2]/option[3]'),
        "error_notification": (By.XPATH, '//*[@class="notifications"]'),
    }
