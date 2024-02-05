from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class ProjectBoxPages(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def no_lamb_flavour_icon(self):
        self.assert_element_not_visible('//*[@alt="signup-flavour-lamb"]')

    def no_chicken_flavour_icon(self):
        self.assert_element_not_visible('//*[@alt="signup-flavour-chicken"]')

    def check_claim_essentials(self, _product, _claim):
        item = self.find_xpath(f"//div[@data-testid='{_product}']//div[@class='product-claim']")
        assert item.text == _claim

    def product_not_shown(self, _product):
        item = self.find_xpath(f"//div[@data-testid='{_product}']")
        item.assert_element_not_visible()

    locator_dictionary = {
        # kibble selection page
        "dry_wet_radiobutton": (By.XPATH, "//*[@id='dry-wet']"),
        # The below two elements are kinda the same radio button
        # but appear differently based on feeding flow:
        # When Dry only in current food flow is selected this element is used:
        "dry_only_radiobutton": (By.XPATH, "//*[@id='dry']"),
        # When Dry and wet food in current food flow is selected this element is used:
        "dry_only_order_with_wetfood_radiobutton": (By.XPATH, "//*[@id='dry-own-wet']"),
        "add_to_box_button": (By.XPATH, "//*[@data-testid='complete-step']"),

        "claims": (By.XPATH, "//*[@class='top-level-claims-wrapper']"),
        "dry_ingredient": (By.XPATH, "//*[@id='__layout']//summary/span[contains(text(),'Ingredients')]"),
        "dry_ingredients": (
            By.XPATH, "//*[@id='__layout']/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/details[1]/div/p"),
        "fr_dry_ingredients": (By.XPATH, "//*[@id='__layout']//summary/span[contains(text(),'Ingrédients')]"),
        "de_dry_ingredients": (By.XPATH, "//*[@id='__layout']//summary/span[contains(text(),'Zutaten')]"),
        "nl_dry_ingredients": (By.XPATH, "//*[@id='__layout']//summary/span[contains(text(),'Ingrediënten')]"),
        # wet food selection page,
        "wet_food_card": (By.XPATH, "//*[@data-testid='tray-name']"),

        "treats_card": (By.XPATH, "//*[@class='container']"),

        "essentials_card": (By.XPATH, "//*[@class='container']"),

        "change_flavours_button": (
            By.XPATH, "//*[@class='button secondary']//span[contains(text(),'{Change flavours/textures}')]"),
        "choose_this_selection_button": (By.XPATH, "//*[@data-testid='complete-step']"),
        "view_feeding_plan_notification_link": (By.XPATH, "//*[@class='cx-link']"),

        # treats selection page
        "go_to_box_button": (By.XPATH, "//*[@data-testid='complete-step']"),
        "dental_dailies_add_gb": (By.XPATH, "//*[@data-testid='medium-dental-dailies']//button[@type='button']"),
        "dental_dailies_add_de": (
            By.CSS_SELECTOR, "div[data-testid='dental-daily-medium-de'] div[class='product-cta']"),
        "dental_dailies_add_roe": (
            By.CSS_SELECTOR, "div[data-testid='tailscom-medium-dental-dailies'] div[class='product-cta']"),
        "treats_claims": (By.XPATH, "//div[@class='claims-wrapper']"),

        "add_promo": (By.XPATH, "//*[@for='tounge']/span[@class='offer-text']"),
        "input_code": (By.XPATH, "//*[@id='code']"),
        "apply_promo": (By.XPATH, "//*[@data-ga-label='tongue-submit']"),

        "dry_own_wet_radiobutton": (By.XPATH, "//*[@for='dry-own-wet']"),
        "dry_only_radiobutton_roe": (By.ID, "dry"),
        "dry_wet_radiobutton_fr": (By.XPATH, "//*[@for='dry-wet']"),
        "see_wet_food": (By.XPATH, "//*/button[@data-testid='see-wet-food']"),
        "see_wet_food_fr": (By.XPATH, "//*/button[@data-testid='see-wet-food']"),
        "wet_page_header": (By.XPATH, "//*[@data-testid='step-header']"),
        "core_diet_header": (By.XPATH, "//div[@class='hero-header-wrapper']//p[1]"),
        "treat_page_header": (By.XPATH, "//div[@class='step-header']/h1"),
        "essentials_page_header": (By.XPATH, "//*[@class='header only-essentials']"),
        "core_diet_page": (By.XPATH, "//*[@class='main-content-container']"),

        "remove_wet_food": (By.XPATH, "//*[@class='remove-wet']"),
        "wet_food_upsell_widget": (By.XPATH, "//*[@class='section upsell-widget']"),
        "see_wet_food_upsell": (By.XPATH, "//*[@class='upsell-cta']"),
        "dry_own_wet_message": (By.XPATH, "//*[@class='portion-message']"),
        "change_wet_food_flavours_textures": (
            By.XPATH, "//*[@id='__layout']/div/div/div[2]/div[1]/div[3]/details/summary/span"),
        "chicken_flavour_radio": (By.XPATH, "//*[@id='chicken']"),
        "lamb_flavour_radio": (By.XPATH, "//*[@id='lamb']"),
        "pate_texture_radio": (By.XPATH, "//*[@id='pate']"),
        "confirm_new_wet_food_selection": (By.XPATH, "//*[@data-testid='change-flavours-textures']"),
        "wet_food_selection_cards": (By.XPATH, "//*[@class='product-info-wrapper']"),
        "close_notification": (By.XPATH, "//*[@class='close icon']"),
        "back_button": (By.XPATH, "//div[@class='hero-back']"),
        "fish_flavour_icon": (By.XPATH, "//*[@alt='signup-flavour-fish']"),
        "beef_flavour_icon": (By.XPATH, "//*[@alt='signup-flavour-beef']"),
        "lamb_flavour_icon": (By.XPATH, "//*[@alt='signup-flavour-lamb']"),
        "chicken_flavour_icon": (By.XPATH, "//*[@alt='signup-flavour-chicken']"),
        "superfood_add": (By.XPATH, "//*[@data-testid='super-lamb-bites']//button[@type='button']"),
        "good_dog_add": (By.XPATH, "//*[@data-testid='good-dog-treats']//button[@type='button']"),
        "poo_bags_add": (By.XPATH, "//*[@data-testid='poo-bags-recycled']//button[@type='button']"),
        "chicken_biscuts_add": (By.XPATH, "//*[@data-testid='chicken-biscuits']//button[@type='button']"),
        "duck_biscuits_add": (By.XPATH, "//*[@data-testid='duck-biscuits']//button[@type='button']"),
        "cold_pressed_add": (By.XPATH, "//*[@data-testid='cold-pressed-duck']//button[@type='button']"),
        "salmon_biscuits_add": (By.XPATH, "//*[@data-testid='salmon-biscuits']//button[@type='button']"),
        "pork_biscuits_add": (By.XPATH, "//*[@data-testid='pork-biscuits']//button[@type='button']"),
        "fresh_chews_medium_add": (By.XPATH, "//*[@data-testid='fresh-chews-medium']//button[@type='button']"),
        "yakers_medium_add": (By.XPATH, "//*[@data-testid='yakers-chew-medium']//button[@type='button']"),
        "natural_chew_add": (By.XPATH, "//*[@data-testid='natural-chews-pig-ears']//button[@type='button']"),
        "good_dog_add_fr": (By.XPATH, "//*[@data-testid='good-dog-treats-fr']//button[@type='button']"),
        "good_dog_add_de": (By.XPATH, "//*[@data-testid='good-dog-treats-de']//button[@type='button']"),
        "salmon_biscuits_fr": (By.XPATH, "//*[@data-testid='salmon-biscuits-fr']//button[@type='button']"),
        "dental_dailies_add_fr": (By.XPATH, "//*[@data-testid='dental-daily-medium-fr']//button[@type='button']"),
        "duck_biscuits_de": (By.XPATH, "//*[@data-testid='duck-biscuits-de']//button[@type='button']"),
        "natural_chew_de_add": (By.XPATH, "//*[@data-testid='natuerliche-kausnacks-schweineohren']//button[@type='button']"),
        "wet_food_accordion": (By.XPATH, "//*[@data-testid='wet-food-options-accordion']"),

    }
