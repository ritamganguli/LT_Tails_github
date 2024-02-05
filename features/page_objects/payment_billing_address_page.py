from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from .base_page_object import BasePage


class BillingAddressTestData:
    def __init__(self):
        self.address_details = \
            {
                "UK":
                    {
                        "postcode": "TW9 2SS",
                        "first_line": "7 Kew Foot Road",
                        "city": "London"
                    },
                "NI":
                    {
                        "postcode": "BT55 7GE",
                        "first_line": "37 Old Mill Grange",
                        "city": "Belfast"
                    },
                "FR":
                    {
                        "postcode": "69008",
                        "first_line": "26 Boulevard de Etats-Unis",
                        "city": "Paris"
                    },
                "DE":
                    {
                        "postcode": "01076",
                        "first_line": "Messedamm 18",
                        "city": "Dresden"
                    },
                "NL":
                    {
                        "postcode": "2541 VJ",
                        "first_line": "Maartensdijklaan 45",
                        "city": "Den Haag"
                    },
                "IE":
                    {
                        "postcode": "BT54 6HX",
                        "first_line": "14 Princes St",
                        "city": "Cork"
                    },
                "AT":
                    {
                        "postcode": "2500",
                        "first_line": "Freisinger, Gaminger Berg 3",
                        "city": "Baden"
                    },
                "BE":
                    {
                        "postcode": "1070",
                        "first_line": "Herentalsebaan 69",
                        "city": "Brussel"
                    },
                "DK":
                    {
                        "postcode": "7200",
                        "first_line": "Fynshovedvej 40",
                        "city": "Grindsted"
                    },
                "SE":
                    {
                        "postcode": "91231",
                        "first_line": "20 Dalagatan",
                        "city": "Vilhelmina"
                    }

            }


class BillingAddressPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    # Re-usable function to add PAN, Expiry date and CVC
    def input_test_card_payment_details(self):
        time.sleep(7)
        with self.iframe("#card-number iframe"):
            self.card_number_input.send_keys("4242424242424242")

        with self.iframe("#card-expiry iframe"):
            self.expiry_date_input.send_keys("1024")

        with self.iframe("#card-cvc iframe"):
            self.cvc_input.send_keys("111")

    # Select billing address flow using address finder by postcode
    # Relevant for UK and NI address pages
    def add_billing_address_with_postcode_lookup(self, country):
        billing_address = BillingAddressTestData()
        time.sleep(3)
        self.no_radiobutton.click()
        time.sleep(10)

        element_one = self.postcode_textbox_billing
        element_one.send_keys(billing_address.address_details[country]["postcode"])
        self.browser.execute_script("document.activeElement.blur();")
        time.sleep(1)
        self.postcode_search_button.click()
        time.sleep(1)
        Select(self.address_select).select_by_visible_text(
            billing_address.address_details[country]["first_line"])

    # Manual input of addresses, this form is used in FR, DE, and ROE
    # UK,NI can use this form as well when Loqate feature is disabled
    def add_billing_address_with_manual_address_input(self, country):
        billing_address = BillingAddressTestData()
        time.sleep(3)
        self.no_radiobutton.click()
        time.sleep(1)
        self.address_first_line_input.send_keys(billing_address.address_details[country]["first_line"])
        time.sleep(1)
        self.address_postcode_manual_input.send_keys(billing_address.address_details[country]["postcode"])
        time.sleep(1)
        self.address_city_input.send_keys(billing_address.address_details[country]["city"])
        time.sleep(1)

    locator_dictionary = {
        "no_radiobutton": (By.CSS_SELECTOR, "label[for=delivery-address-no]"),
        "postcode_textbox": (By.CSS_SELECTOR, "#search-postcode-redesign"),
        "postcode_textbox_billing": (By.CSS_SELECTOR, "#search-postcode-redesign"),
        "postcode_textbox_billing_prev": (By.CSS_SELECTOR, "#search-postcode"),
        "postcode_search_button": (By.CSS_SELECTOR, "a.postcode-lookup"),
        "address_select": (By.ID, 'address-select'),
        "card_number_input": (By.CSS_SELECTOR, "input[name=cardnumber]"),
        "expiry_date_input": (By.CSS_SELECTOR, "input[name=exp-date]"),
        "cvc_input": (By.CSS_SELECTOR, "input[name=cvc]"),
        "checkout_button": (By.CSS_SELECTOR, ".btn.btn-primary.icon-lock"),
        "address_first_line_input": (By.CSS_SELECTOR, "input[name=address-first_line]"),
        "address_postcode_manual_input": (By.CSS_SELECTOR, "input[name=address-postal_code]"),
        "address_city_input": (By.CSS_SELECTOR, "input[name=address-city")

    }
