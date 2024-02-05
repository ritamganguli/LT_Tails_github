from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class ManualWetFoodPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def check_product_available(self):
        # Step 2: Try to find the element and check its visibility
        try:
            element = self.find_element(By.XPATH, "//div/p[contains(text(),'Rich Poultry and Game Hotpot with Duck and Carrots')]")
            if element.is_displayed():
                print("Wet food: Rich Poultry and Game Hotpot with Duck and Carrots IS available")
            else:
                print("Wet food: Rich Poultry and Game Hotpot with Duck and Carrots NOT available - reconfigure step with another product")
        except NoSuchElementException:
            print("Wet food: Product Id 871 - Rich Poultry and Game Hotpot with Duck and Carrots NOT available - reconfigure step with another product")

    locator_dictionary = {
        # select plus button
        "increase_trays_product_871": (By.XPATH, "//*[@data-product-id='871']/div/div[1]/div[2]/button/span"),
        # select again after 1 tray added
        "add_more_trays": (By.XPATH, "//*[@data-product-id='871']/div/div[1]/div[2]/button"),
        # tray is open and minus button select
        "decrease_trays_product_871": (By.XPATH, "//*[@data-product-id='871']/div/div[1]/div[2]/div/div/button[2]"),
        "add_more_trays_input": (By.XPATH, "//*[@id='product_871_quantity']"),
        "recipe_1": (By.XPATH, "//input[@id='product_871_quantity']"),
        "add_wf_button": (By.XPATH, "//span[normalize-space()='Next']"),
        "add_next_delivery": (By.XPATH, "//span[normalize-space()='Add to next delivery']"),
        "wet_food_box_tray": (By.XPATH, "//p[contains(text(),'31 trays')]")

    }