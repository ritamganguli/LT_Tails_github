import time

from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class FrontyardPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def login_fy(self):
        time.sleep(7)
        username = "qa_auto_tests"
        password = "itsasecret"
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.signin.click()

    def get_dss_data_json(self):
        self.number_of_windows(2)
        self.browser.switch_to.window(self.browser.window_handles[1])
        dss_data = self.json_object.text
        return dss_data

    locator_dictionary = {
        "username": (By.XPATH, "//input[@id='username']"),
        "password": (By.XPATH, "//input[@id='password']"),
        "signin": (By.XPATH, "//button[normalize-space()='Sign in']"),
        "forgotemail": (By.XPATH, "//h2[normalize-space()='Emails']"),
        "overview_title": (By.XPATH, "//h2[@class='panel-title']"),
        "search": (By.XPATH, "//input[@placeholder='name / email / mobile / id']"),
        "search_button": (By.XPATH, "//span[@class='fa fa-search']"),
        "contactable": (By.XPATH, "//span[normalize-space()='contactable']"),
        "donotcontact": (By.XPATH, "//span[normalize-space()='do not contact']"),
        "subscription_next_delivery_date": (By.XPATH, "//*[@class='next-delivery-date']"),
        "subscription_checkbox": (By.CSS_SELECTOR, "input[type='checkbox'][name='subscription_id']"),
        "get_email_data": (By.CSS_SELECTOR, "[data-target='#emailDataModal']"),
        "get_dss_data": (By.CSS_SELECTOR, "[value='send_dss']"),
        "json_object": (By.CSS_SELECTOR, "pre"),

    }
