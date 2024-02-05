import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from .base_page_object import BasePage
from selenium.webdriver.support import expected_conditions as EC


class AccountPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    # This method doesn't work with PayPal payment method because the button click is inside the iFrame
    def select_payment_method(self, payment_method):
        getattr(self, f"select_{payment_method}").click()
        getattr(self, f"{payment_method}_checkout").click()

    def select_paypal_payment_method(self):
        time.sleep(5)
        self.select_paypal.click()
        # PayPal button takes a while to fully display after selecting payment method but Selenium thinks it's ready
        time.sleep(10)
        with self.iframe("#paypal-button > div > div > iframe"):
            # This was a last resort, selenium clicks did not work
            self.browser.execute_script("arguments[0].click();", self.paypal_checkout_button)

    def confirm_paypal_payment_method(self):
        time.sleep(5)
        self.confirm_payment_update_button.click()

    # placed the checkout code in this page to call from steps page+
    def checkout_stripe_payment(self):
        time.sleep(10)

        self.wait_for(
            "#payment-details-form",
            EC.presence_of_element_located,
        )

        with self.iframe("#card-number iframe"):
            self.input_text("input[name=cardnumber]", "4242424242424242", typing_delay=0.2)
        time.sleep(1)

        with self.iframe("#card-expiry iframe"):
            self.input_text("input[name=exp-date]", "1024", typing_delay=0.2)

        with self.iframe("#card-cvc iframe"):
            self.input_text("input[name=cvc]", "111", typing_delay=0.2)

    def fr_update_address_logged_in(self):
        time.sleep(5)
        self.update_postcode.clear()
        self.update_postcode.send_keys(
            "69008"
        )
        self.update_first_line.clear()
        self.update_first_line.send_keys(
            "26 Boulevard de Etats-Unis"
        )
        self.update_city.clear()
        self.update_city.send_keys(
            "Lyon"
        )
        self.save_changes_button.click()
        time.sleep(2)

    def de_update_address_logged_in(self):
        time.sleep(5)
        self.update_postcode.clear()
        self.update_postcode.send_keys(
            "01076"
        )
        self.update_first_line.clear()
        self.update_first_line.send_keys(
            "Messedamm 18"
        )
        self.update_city.clear()
        self.update_city.send_keys(
            "Dresden"
        )
        self.save_changes_button.click()
        time.sleep(2)

    def update_special_instructions(self, special_instruction):
        Select(self.special_instruction_select).select_by_visible_text(special_instruction)

    def dpd_check(self):
        try:
            self.find_element(By.XPATH, "//input[@type='radio' and @data-courier='dpd' and @checked]")
            print("DPD Radio button is selected.")
        except NoSuchElementException:
            # Exception occurs if there is no selected radio button
            print("DPD Radio button is not selected.")

    def select_address_dropdown_deliver_address(self, address):
        time.sleep(5)
        # Use WebDriverWait to wait for the dropdown to be present
        wait = WebDriverWait(self.browser, 30)
        dropdown_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="address-select"]')))

        # Once the dropdown is present, wrap it in a Select object
        dropdown = Select(dropdown_element)

        # Check if the option 'Python' is present in the dropdown
        option_present = any(option.text == address for option in dropdown.options)
        assert option_present, address

        # Select the 'Python' option
        dropdown.select_by_visible_text(address)

    def select_address_dropdown_card_not_deliver_address(self, address):
        time.sleep(5)
        # Use WebDriverWait to wait for the dropdown to be present
        wait = WebDriverWait(self.browser, 30)
        dropdown_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="address-select"]')))

        # Once the dropdown is present, wrap it in a Select object
        dropdown = Select(dropdown_element)

        # Check if the option 'Python' is present in the dropdown
        option_present = any(option.text == address for option in dropdown.options)
        assert option_present, address

        # Select the 'Python' option
        dropdown.select_by_visible_text(address)

    locator_dictionary = {
        "account_page_header": (By.XPATH, "//*[@class='account-settings-title']"),
        "account_flash_message_notification": (By.XPATH, "//*[@class='notification-content ']/p"),
        "update_delivery": (By.XPATH, "//a[@href='/gb/settings/delivery-address']"),
        "update_recipient_name": (By.XPATH, "//*[@id='address-recipient_name']"),
        "delivery_address": (By.XPATH, "//*[@class='input-wrapper']/span[contains(text(),'Kew Foot')]"),
        "change_address": (By.XPATH, "//*[@class='change-address']"),
        "search_postcode": (By.XPATH, "//*[@id='search-postcode-redesign']"),
        "search_postcode_old_design": (By.XPATH, "//*[@id='search-postcode']"),
        "Dpd_delivery_service_option": (By.XPATH, "//ul/li/label/div/div[contains(text(),'Named day')]"),
        "find_address": (By.XPATH, "//*[@class='postcode-lookup postcode-lookup-redesign btn btn-secondary redesign']"),
        "find_address_old_design": (By.XPATH, "//*[@class='postcode-lookup']"),
        "find_address_link": (By.XPATH, "//*/div/a[contains(text(),'Find address')]"),
        "new_address": (By.XPATH, "//*[@id='address-select']"),
        "select_new_address": (By.XPATH, "//*[@id='address-select']/option[2]"),
        "save_changes_button": (By.XPATH, "//*[@id='next_btn']"),
        "address_account_page": (By.XPATH, "//p[@data-testid='address-account-page']"),
        "update_payment_button": (By.XPATH, "//*[@data-testid='update-payment-method-cta']"),
        "delivery_service_account_page": (By.XPATH, "//input[@type='radio' and @data-courier='dpd' and @checked]"),
        "special_instructions_account_page": (By.XPATH, "//p[@datatest-id='special-delivery-instructions-account-card']"),
        "special_instruction_select": (By.XPATH, "//select[@name='address-delivery_instruction_id']"),
        "phone_country_code": (By.ID, "address-mobile_calling_code"),
        "phone_number": (By.ID, "address-mobile_phone"),
        "select_paypal": (By.XPATH, "//*[@class='radio-toggle-button paypal ']"),
        "select_stripe": (By.XPATH, "//*[@class='radio-toggle-button stripe ']"),
        "paypal_checkout": (By.ID, "paypal-button"),
        "stripe_checkout": (By.XPATH, "//*[@type='submit']"),
        "confirm_card_details_stripe": (By.XPATH, "//button[@type='submit']"),
        "card_payment_details": (By.XPATH, "//*[@data-testid='card-payment-details']"),
        "card_expiry_details": (By.XPATH, "//*[@data-testid='expiry-details']"),
        "paypal_logo": (By.XPATH, "//*[@alt='PayPal logo']"),
        "stripe_page_header": (By.CSS_SELECTOR, "#payment-details-form h1"),
        "paypal_checkout_button": (By.XPATH, "//span[@class='paypal-button-text'][contains(text(),' Checkout')]"),

        "confirm_payment_update_button": (By.XPATH, "//*[@class='btn btn-primary btn-heavy']"),
        "change_password_button": (By.XPATH, "//a[contains(@href,'/settings/change-password/')]"),
        "current_password": (By.XPATH, "//*[@id='password']"),
        "new_password": (By.XPATH, "//*[@id='new_password']"),
        "confirm_new_password": (By.XPATH, "//*[@id='confirm_new_password']"),
        "save_password_button": (By.XPATH, "//*[@class='btn btn-primary']"),

        "account_page_notification": (By.XPATH, "//*[@id='notifications']"),

        "different_billing": (By.XPATH, "//*[@id='delivery-address-no']"),
        "same_billing": (By.XPATH, "//*[@id='delivery-address-yes']"),

        "update_details": (By.XPATH, "//a[contains(@href,'/settings/details')]"),
        "email_account": (By.XPATH, "//*[@name='email']"),
        "save_details": (By.XPATH, "//*[@type='submit']"),

        "cancel_link": (By.XPATH, "//a[contains(@href,'/cancel')]"),
        "cancel_cta": (By.XPATH, "//a[contains(@href,'/rt-offboarding-reasons')]"),
        "food_reason_cancel": (By.XPATH, "//a[contains(@href,'/issue_with_food')]"),
        "confirm_cancel": (By.XPATH, "//*[@class='btn btn-secondary confirm-cancel-button']"),
        "deliveries_cancelled": (By.XPATH, "//*[@class='panel-white clearfix']"),

        "update_comms_button": (By.XPATH, "//a[@href='/gb/settings/communication-preferences']"),
        "comms_save_button": (By.XPATH, "//button[normalize-space()='Save']"),
        "comms_sub_heading": (By.XPATH, "//p[@class='sub-heading']"),
        "comms_privacy": (By.LINK_TEXT, "Privacy policy"),
        "update_postcode": (By.XPATH, "//*[@id='address-postal_code']"),
        "update_city": (By.XPATH, "//*[@id='address-city']"),
        "update_first_line": (By.XPATH, "//*[@id='address-first_line']"),
        "unclaimed": (By.XPATH, "//*[@class='title'][contains(text(),'credit')]"),
        "select_credit_card": (By.XPATH, "//span[contains(text(),'Credit/Debit card')]"),
        "continue_pay_method_button": (By.XPATH, "//button[@type='submit'][contains(text(),'Continue')]"),
        "card_register_address_find": (By.XPATH, "//*[@data-testid='find-my-address-button']"),
        "paypal_different_billing": (By.XPATH, "//*[@for='delivery-address-no']"),
        "paypal_different_billing_postcode_search": (By.XPATH, "//*[@data-testid='postcode-search-field']"),
        "select_billing_address_dropdown_card": (By.XPATH, "//*[@data-testid='select-address-dropdown-address']"),
        "select_billing_address_dropdown_address": (By.XPATH, "//*[@id='address-select']"),
        "billing_address_manual": (By.XPATH, "//*[@data-testid='select-address-address-manual']"),
        "address_manual_company": (By.XPATH, "//*[@data-testid='address-manual-company']"),
        "address_manual_first_line": (By.XPATH, "//*[@data-testid='address-manual-first-line']"),
        "address_manual_second_line": (By.XPATH, "//*[@data-testid='address-manual-second-line']"),
        "address_manual_third_line": (By.XPATH, "//*[@data-testid='address-manual-third-line']"),
        "address_manual_postcode": (By.XPATH, "//*[@data-testid='address-manual-postcode']"),
        "address_manual_city": (By.XPATH, "//*[@data-testid='address-manual-city']"),
    }
