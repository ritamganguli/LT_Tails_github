import os
import sys
import time
import secrets

import string
import requests
from selenium.webdriver.common.by import By
from .base_page_object import BasePage
import shared


class EmailPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def create_random_email(self):
        strong_random = self.strong_randomise_email()
        self.email_input.send_keys(strong_random)

    def create_random_email_suitability(self, petname):
        strong_random = self.strong_randomise_suitability_email()
        self.email_input.send_keys(strong_random)

    def create_random_email_prod(self):
        strong_random = self.strong_randomise_email()
        self.email_input.send_keys(strong_random)

    def country_for_login(self, country):
        country_id = "gb"
        if country == "France": country_id = "fr"
        if country == "Deutschland": country_id = "de"
        self.goto(f"/{country_id}/signin")

    @staticmethod
    def strong_randomise_email():
        # Define character set to include lowercase, uppercase, and digits
        chars = string.ascii_letters + string.digits

        # Generate a more random and longer string
        random_string = ''.join(secrets.choice(chars) for _ in range(7))  # Adjust range for desired length

        # Create the email string
        email_address = f"{random_string}auto@example.com"

        return email_address

    @staticmethod
    def strong_randomise_suitability_email():
        # Define character set to include lowercase, uppercase, and digits
        chars = string.ascii_letters + string.digits

        # Generate a more random and longer string
        random_string = ''.join(secrets.choice(chars) for _ in range(7))  # Adjust range for desired length

        # Create the email string
        email_address = f"{random_string}@suitability.com"

        return email_address

    def get_email_account(self, seed_profile_type, store_id):
        # if config.Config.should_execute_specific_code() and shared.browser in ("chrome", "iphone", "android"):
        if shared.browser in ("chrome", "iphone", "android"):
            fy_hyper_url = self.fy_hyper_url

            # Create a session
            session = requests.Session()

            # Define the proxies and assign to the session
            proxy = {
                'http': os.getenv('LT_PROXY_HOST') + ':' + os.getenv('LT_PROXY_PORT'),
                'https': os.getenv('LT_PROXY_HOST') + ':' + os.getenv('LT_PROXY_PORT'),
            }

            session.proxies = proxy

            # Define login URL and credentials
            login_url = f"{fy_hyper_url}/login"
            credentials = {
                "username": "qa_auto_tests",
                "password": "itsasecret"
            }

            # Making the POST request using session
            login_response = session.post(login_url, data=credentials, verify=False)
            print(login_response)
            print(login_response.status_code)

            cookie = login_response.headers.get('Set-Cookie')
            print(cookie)

            # Define URL for the second POST request
            seed_url = f"{fy_hyper_url}/qa_seeds/new_customer/{seed_profile_type}/{store_id}"

            # Setup headers with the cookie
            headers = {
                'Cookie': f'Cookie_2=value; {cookie}',

            }

            # Define data for the POST request
            data = {'tier': 'superpremium'}

            # Making the POST request using session
            post_response = session.post(seed_url, headers=headers, data=data, verify=False)

            # Printing the POST response
            print(post_response.text)

            email = post_response.content.decode("utf-8")
            return email

        else:
            fy_url = self.fy_url
            # seed_profile_type parameter: active / paused / cancelled
            # store_id: Can be found here https://frontyard.tails-nonprod.com/store/
            seed_url = f"{fy_url}/qa_seeds/new_customer/{seed_profile_type}/{store_id}"
            login_url = f"{fy_url}/login"
            credentials = {"username": "qa_auto_tests", "password": "itsasecret"}
            login_result = requests.post(
                login_url,
                credentials
            )
            cookie = login_result.request.headers['cookie']
            payload = {
                'tier': 'superpremium'
            }
            headers = {
                'Cookie': f'Cookie_2=value; {cookie}',
            }
            time.sleep(1)
            response = requests.request("POST", seed_url, headers=headers, data=payload)
            print(response.text, file=sys.stderr)
            print(response.status_code, file=sys.stderr)
            email = response.content.decode("utf-8")
            return email

    @staticmethod
    def get_customer_id_from_email(customer_email):
        return customer_email.split('+')[0]

    def email_password(self):
        user_field = self.find_xpath("//*[@id='password']")
        user_field.click()
        user_field.send_keys()
        user_field.click()
        user_field.send_keys(1234)
        time.sleep(10)

    locator_dictionary = {
        "email_form": (By.CSS_SELECTOR, "#form_email"),
        "email_input": (By.CSS_SELECTOR, "#email"),
        "marketing_preference_form": (By.XPATH, "//*[@class='intro email-hidden']"),
        "opt_in_no": (By.CSS_SELECTOR, "label[for=opt_in-1]"),
        "opt_in_yes": (By.CSS_SELECTOR, "label[for=opt_in-0]"),
        "email_error": (By.XPATH, "//*[@class='email-inline-error']"),
        "email_submit": (By.XPATH, "//*[@name='next_btn_email']"),
        "email_login": (By.CSS_SELECTOR, "input[name=email]"),
        "food_ready_uk": (By.XPATH, "//*[@id='form_email']//span[contains(text(),'Dogone')]"),
        "food_ready": (
            By.XPATH,
            "//span[contains(text(),'Dogone')]",

        ),
        "password_dashboard_login": (By.CSS_SELECTOR, "#password"),

        "forgot_password_email": (By.XPATH, "//input[@id='email']"),
        "forgot_password_header": (By.XPATH, "//h1[normalize-space()='Forgotten password?']"),
        "forgot_password_submit": (By.XPATH, "//button[normalize-space()='Submit']"),
        "forgot_password_confirmation": (By.XPATH, "//p[contains(text(),'Please check your email')]"),
        "forgot_password_OK": (By.XPATH, "//a[normalize-space()='Okay']"),
        "getemail": (By.XPATH, "/html/body"),
        "fy_logout": (By.XPATH, "//a[contains(@href,'out')]"),
    }
