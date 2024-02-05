import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from .base_page_object import BasePage


class ShopPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser),

    def warning_close_cookie(self):
        time.sleep(5)
        try:
            if self.find('#cookie_prompt a[href="#"]'):
                self.click_element_('#cookie_prompt a[href="#"]')
        except NoSuchElementException:
            pass

    def dismiss_survey(self):
        time.sleep(5)
        try:
            if self.find('#Page-1'):
                self.click_element_('#Page-1')
        except NoSuchElementException:
            pass

    def product(self, product_):
        return self.find_xpath(f"//*/div[2]/div[1]/div[1][contains(text(),'{product_}')]")

    def get_current_url(self):
        return self.browser.current_url

    def is_url_matching(self, expected_url):
        current_url = self.get_current_url()
        return current_url == expected_url

    def go_to_product_pdp_by_name(self, _product):
        product_dict = {
            "poo bags": '/poo-bags-recycled',
            "hemp rope toy": '/hemp-rope-toy',
            "natural chews": '/natural-chews-pig-ears',
        }
        product_ = product_dict[_product.lower()]
        self.find_xpath(f"//*[contains(@href,'{product_}')]").click()

    locator_dictionary = {
        "shop_header": (By.XPATH, "//*[@class='product'][contains(text(),'tails.com dry food')]"),
        "order_details": (By.XPATH, "//*[@id='tails-view-3'']/div/table/tbody/tr[2]/td[1]/a"),
        "chicken_biscuits_delivery": (By.XPATH, "//h3[contains(text(),'Chicken Biscuits')]"),
        "biscuits_header": (By.XPATH, "//*[@class='title']"),
        "save_selection": (By.XPATH, "//*[@class='btn btn-primary save']"),
        "next_delivery": (By.XPATH, "//*[@class='details']/span[contains(text(),' Next order contains ')]"),
        "add_salmon_biscuits": (By.XPATH, "//div[@id='salmontreats']"),
        "edit_salmon_biscuits": (By.XPATH, "//div[@id='salmontreats']//label[@for='salmon-treats']"),
        "pause_salmon_biscuits": (By.XPATH, "//*[contains(@href,'/salmon_treats_pause/')]"),
        "pause_reason": (By.XPATH, "//*[@for='option-102']"),
        "confirm_reason": (By.XPATH, "//*[@class='btn btn-primary next']"),
        "saved_quantity": (By.XPATH, "//*[@class='quantity disabled']"),
        "products_receiving": (By.XPATH, "//*[@id='top-element']/article/div/header/div[1]/button/span[2]"),

        "wet_food_add_button": (By.XPATH, "//*[@data-testid='product-tile-title'][contains(text(),'Wet food')]"),
        "wet_food_edit_button": (By.CSS_SELECTOR, "div[id='tails-view-24'] a[class='btn btn-primary'] "),
        "shop_now_button": (By.CSS_SELECTOR, "div.actions"),
        "wet_food_header": (By.XPATH, "//*[@class='hero-text']"),
        "save_my_selection": (By.CSS_SELECTOR, "#tails-view-1 > button"),
        "choose_my_tray": (By.CSS_SELECTOR, "a[href*='/wet-food-selection/manual']"),
        "select_wet_flavours": (By.XPATH, "//*[contains(@href,'wet-food-pet')]"),
        "add_amount": (By.XPATH, "//*[contains(@href,'/wet-portion')]"),
        "surprise_flavours": (By.XPATH, "//*[@data-mode='automatic']"),
        "confirm_wet_trays": (By.XPATH, "//*[@class='btn btn-primary checkout']"),
        "switch_150gr_tray": (By.XPATH, ".//input[@type='radio' and @value='150']"),
        "switch_300gr_tray": (By.XPATH, ".//input[@type='radio' and @value='300']"),
        "add_to_delivery": (By.XPATH, "//*[@class='btn btn-primary order-wet-food']"),
        "order_summary": (By.XPATH, "//div[2]/div[1]/div[1]"),
        "yes_button": (By.XPATH, "//*[@class='btn btn-primary']"),
        "add_chicken_biscuits": (By.XPATH, "//div[@id='chickentreats']//a[@class='action btn btn-primary add']"),
        "edit_chicken_biscuits": (By.XPATH, "//div[@id='chickentreats']//label[@for='chicken-treats']"),
        "pause_chicken_biscuits": (By.XPATH, "//*[contains(@href,'/chicken-treats/stop')]"),
        "wet_food_name": (By.CSS_SELECTOR, "div > div.top > p"),
        "product_delivery": (By.XPATH, "//*[@class='col-food']"),
        "add_delivery": (By.XPATH, "//button/span[contains(text(),'Add to deliveries')]"),
        "simply_delicious_beef_with_parsley": (
        By.XPATH, "//*[@class='product']//*[contains(text(),'Simply Delicious Beef with Parsley')]"),
        "tender_terrine_with_chicken_turkey_peas": (
        By.XPATH, "//*[@class='product']//*[contains(text(),'Tender terrine with chicken turkey peas')]"),
        "simply_irresistible_chicken_with_rosemary": (
        By.XPATH, "//*[@class='product']//*[contains(text(),'Simply Irresistible Chicken with Rosemary')]"),
        "succulent_poultry_pie_with_green_beans": (
        By.XPATH, "//*[@class='product']//*[contains(text(),'Succulent Poultry Pie with Green Beans')]"),
        "view_excluded_wet_hypo": (By.XPATH, "//div[1]/p[contains(text(),'wheat and beef have been excluded')]"),
        "view_excluded_wet_puppy_wheat": (By.XPATH, "//div[1]/p[contains(text(),'wheat has been excluded')]"),
        "wet_food_image": (By.XPATH, "//img[@alt='Wet Collection']"),
        "natural_chews_add_gb": (By.XPATH, "//*[@data-testid='product-tile-link-natural-chews-pig-ears']//button[@class='tails-cta tails-cta-icon primary quick-add-btn']"),
        "add_subscription": (By.XPATH, "//*[@data-testid='add-to-box-button']"),
        "octopus_add": (By.XPATH,"//*[@data-testid='product-tile-link-ollie-the-octopus']//button[@class='tails-cta tails-cta-icon primary quick-add-btn']"),
        "hamburger_menu": (By.XPATH, "//*[normalize-space()='Menu']//*[name()='svg']"),
        "deliveries_icon": (By.XPATH, "//*[contains(@href,'deliveries')]"),
        "poo_bags_add": (By.XPATH, "//*[@data-testid='product-tile-link-poo-bags-recycled']//button[@class='tails-cta tails-cta-icon primary quick-add-btn']"),
        "rope_ball_add": (By.XPATH, "//*[@data-testid='product-tile-link-beco-hemp-rope-toy']//button[@class='tails-cta tails-cta-icon primary quick-add-btn']"),
        "chicken_biscuits_add": (By.XPATH, "//*[@data-testid='product-tile-link-chicken-biscuits']//button[@class='tails-cta tails-cta-icon primary quick-add-btn']"),
        "duck_biscuits_add": (By.XPATH, "//*[@data-testid='product-tile-link-duck-biscuits']//button[@class='tails-cta tails-cta-icon primary quick-add-btn']"),
        "cold_press_duck_add": (By.XPATH, "//*[@data-testid='data-testid='product-tile-link-super-duck-bites']//button[@class='tails-cta tails-cta-icon primary quick-add-btn']"),
        "shop_content": (By.XPATH, "//*[@class='content']"),
        "pdp_title": (By.XPATH, "//*[@data-testid='product-title-title']"),
        "counter_minus": (By.XPATH, "//*[@data-testid='counter-minus']"),
        "products_receiving_dropdown": (By.XPATH, "//*[@data-testid='accordion-title']"),
    }
