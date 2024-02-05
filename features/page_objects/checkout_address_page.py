import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page_object import BasePage


class CheckoutAddressPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def address_select_uk(self):
        time.sleep(7)
        self.select_by_text("#address-select", "7 Kew Foot Road")

    def address_select_interim(self):
        time.sleep(5)
        self.select_by_text("#address-select", "19 Islandarragh Road")

    def address_select_uk_prod(self):
        time.sleep(5)
        self.select_by_text("#address-select", "Tails Co, Spencer House, 23 Sheen Road")

    def address_select_ni(self):
        time.sleep(5)
        self.select_by_text("#address-select", "37 Old Mill Grange")

    def add_address_for_country(self, your_country):
        CheckoutAddressPage.__dict__[f'address_{your_country.lower()}'](self)

    def address_sweden(self):
        time.sleep(5)
        self.find_xpath('//*[@id="address-postal_code"]').send_keys("91231")
        self.find_xpath('//*[@id="address-first_line"]').send_keys("20 Dalagatan")
        self.find_xpath('//*[@id="address-city"]').send_keys("Vilhelmina")

    def address_france(self):
        time.sleep(5)
        self.find_xpath('//*[@id="address-postal_code"]').send_keys("69008")
        self.find_xpath('//*[@id="address-first_line"]').send_keys("26 Boulevard de Etats-Unis")
        self.find_xpath('//*[@id="address-city"]').send_keys("Lyon")

    def address_denmark(self):
        time.sleep(5)
        self.find_xpath('//*[@id="address-postal_code"]').send_keys("7200")
        self.find_xpath('//*[@id="address-first_line"]').send_keys("Fynshovedvej 40")
        self.find_xpath('//*[@id="address-city"]').send_keys("Grindsted")

    def address_belgium(self):
        time.sleep(5)
        self.find_xpath('//*[@id="address-postal_code"]').send_keys("1070")
        self.find_xpath('//*[@id="address-first_line"]').send_keys("Herentalsebaan 69")
        self.find_xpath('//*[@id="address-city"]').send_keys(" Brussel")

    def address_ireland(self):
        time.sleep(5)
        self.find_xpath('//*[@id="address-city"]').send_keys("Cork")
        self.find_xpath('//*[@id="address-first_line"]').send_keys("14 Princes St")

    def address_netherlands(self):
        time.sleep(5)
        self.find_xpath('//*[@id="address-first_line"]').send_keys(
            "Maartensdijklaan 45"
        )
        self.find_xpath('//*[@id="address-postal_code"]').send_keys("2541 VJ")
        self.find_xpath('//*[@id="address-city"]').send_keys("Den Haag")

    def address_germany(self):
        time.sleep(10)
        self.find_xpath('//*[@id="address-postal_code"]').send_keys("01076")
        self.find_xpath('//*[@id="address-first_line"]').send_keys("Messedamm 18")
        self.find_xpath('//*[@id="address-city"]').send_keys("Dresden")

    def address_austria(self):
        time.sleep(5)
        self.find_xpath('//*[@id="address-postal_code"]').send_keys("2500")
        self.find_xpath('//*[@id="address-first_line"]').send_keys(
            "Freisinger, Gaminger Berg 3"
        )
        self.find_xpath('//*[@id="address-city"]').send_keys("Baden")

    def future_delivery_date(self):
        time.sleep(5)
        future_dates = Select(self.find_xpath("//*[@id='your_first_delivery-delivery_date']"))
        time.sleep(7)
        future_dates.select_by_index(10)

    def fr_future_delivery_date(self):
        wait = WebDriverWait(self.driver, 50)
        future_dates_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='your_first_delivery"
                                                                                    "-delivery_date']")))
        future_dates = Select(future_dates_element)
        future_dates.select_by_index(4)

    def remote_address_select(self):
        time.sleep(5)
        self.select_by_text("#address-select", "Ashlea, Rosemount Farm, Parkhead Road")

    locator_dictionary = {
        "delivery_details": (By.CSS_SELECTOR, "#signup-delivery-details"),
        "first_name": (By.XPATH, '//*[@id="first"]'),
        "last_name": (By.XPATH, '//*[@id="last"]'),
        "password": (By.CSS_SELECTOR, "input[name=password]"),
        "mobile_number": (By.CSS_SELECTOR, "input[name=mobile_phone]"),
        "address_next": (By.CSS_SELECTOR, ".btn.next"),
        "your_address": (
            By.CSS_SELECTOR,
            ".step[data-step=your-address][data-status=active] form",
        ),
        "search_postcode_prev": (By.CSS_SELECTOR, "#search-postcode"),
        "search_postcode": (By.CSS_SELECTOR, "#search-postcode-redesign"),
        "postcode_lookup": (By.XPATH, "//*[@class='postcode-lookup postcode-lookup-redesign btn btn-secondary redesign']"),
        "address_line": (By.CSS_SELECTOR, "#address-select"),
        # "get_dates": (By.ID, 'get-dates'),
        "get_dates_": (By.XPATH, '//*[@id="tails-view-19"]/button[1]'),
        "get_dates_de": (By.ID, 'get-dates'),
        "next": (By.CSS_SELECTOR, "form .btn.btn-primary[type='submit']"),
        "next_de": (By.XPATH, '//span[contains(text(),"Weiter")]'),
        "delivery_dates": (By.TAG_NAME, '#your_first_delivery-delivery_date'),
        "fr_delivery_dates": (
            By.XPATH,
            '//*[@id="your_first_delivery-delivery_date"]',

        ),
        "inter_postcode": (By.CSS_SELECTOR, "#address-postal_code"),
        "first": (By.XPATH, "//*[@id='address-select']/option[2]"),
        "city": (By.XPATH, '//*[@id="address-city"]'),
        "domicile": (By.XPATH, '//*[@id="delivery-methods"]/div/div[1]/div'),
        "fr_postcode": (By.XPATH, '//*[@id="delivery-address"]/div/form/div[4]/input'),
        "fr_get_dates": (
            By.XPATH,
            '//*[@id="delivery-address"]/div/form/div[7]/div[1]/'
            'button[contains(text(),"Voir les dates de livraison")]',

        ),
        "opt_out_phone": (By.XPATH, '//*[@for="opt_in_phone-False"]'),
        "opt_out_text": (By.XPATH, '//*[@for="opt_in_text_message-False"]'),
        "opt_in_email": (By.XPATH, '//*[@for="opt_in-True"]'),
        "opt_out_email": (By.XPATH, '//*[@for="opt_in-False"]'),
        "man_post_code": (By.CSS_SELECTOR, "#address-postal_code"),
        "first_line": (By.CSS_SELECTOR, "#address-first_line"),
        "man_city": (By.CSS_SELECTOR, "#address-city"),
        "checkout_securely": (By.XPATH, "//button/span[contains(text(),'Check out securely')]"),
        "search_postcode_redesign": (By.CSS_SELECTOR, "#search-postcode-redesign"),
        "postcode_lookup_redesign": (By.XPATH, "//*[@class='postcode-lookup postcode-lookup-redesign btn btn-white']"),
        "card_page_check": (By.XPATH, "//*[@class='step-content'][contains(text(), 'Zahlung')]"),
        "change_address_button": (By.CSS_SELECTOR, '[data-action="change-address"]'),
        "get_dates": (By.XPATH, '//*[@id="get-dates"]'),
        "following_dates_selection_page": (By.XPATH, '//*[@class="btn btn-primary redesign btn-heavy next"]'),
        "generic_address_next": (By.XPATH, '//*[@class="btn btn-primary redesign btn-heavy next"]'),
        "next_fr": (By.XPATH, '//*[@class="btn btn-primary redesign btn-heavy next"]'),

    }
