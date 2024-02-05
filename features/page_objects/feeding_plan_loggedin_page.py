from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class FeedingPage(BasePage):
    amount_locator_id = "amount"

    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def get_treat_option_element(self, option):
        if option == "Occasionally":
            return self.treats_choice_occasionally_radio

    locator_dictionary = {
        "feeding_plan_page_header": (By.XPATH, "//*[@class=' portions icons-info-scope']/div[1]"),
        "update_portions_link": (By.XPATH, "//a[contains(@href,'/wet-portion')]"),
        "wet_portion_form": (By.ID, "wet-portion"),
        "plus_icon": (By.ID, "plus"),
        "radio_buttons_group": (By.ID, "radio-form"),
        "tray_fractions": (By.CSS_SELECTOR, "#amount"),
        "treats_portion_options": (By.CSS_SELECTOR, ".radio-buttons.left > div"),
        "recommended": (By.XPATH, "//*[@class='sub-heading bold']"),
        "increase_tray_size_icon": (By.CSS_SELECTOR, "#plus"),
        "decrease_tray_size_icon": (By.CSS_SELECTOR, "#minus"),
        "next_button": (By.ID, "next_btn"),
        "tray_size_all_options": (By.CSS_SELECTOR, "#amount > option:nth-child(n)"),
        "treats_choice": (By.XPATH, "//*[@for='other-portion-0']"),
        "treats_choice_not_really_radio": (By.CSS_SELECTOR, "#radio-form [for='other-portion-0'] span"),
        "treats_choice_occasionally_radio": (By.CSS_SELECTOR, "#radio-form [for='other-portion-3'] span"),
        "treats_choice_quite_a_bit_radio": (By.CSS_SELECTOR, "#radio-form [for='other-portion-8'] span"),
        "treats_choice_full_meal_radio": (By.CSS_SELECTOR, "#radio-form [for='other-portion-30'] span"),
        "dry_recommended": (By.CSS_SELECTOR, ".recommended.all-upper"),
        "price_header": (By.XPATH, "//*[@class='price-change-table']/h3"),
        "notification_banner": (By.XPATH, "//*[@class='notification-content ']/p"),
    }
