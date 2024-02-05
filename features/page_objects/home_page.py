import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from .base_page_object import BasePage


class HomePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

        # Set the detected_country to FR in all cases to trigger the country selection
        # page
        self.set_test_url_params(
            {
                "cc": "fr",
            }
        )
        # # Cookies to set in order to control which optimizely test variant
        # # selenium will see during a test run.
        # # 'ngt_box_test:default' as the value = default flow
        # # 'ngt_box_test:b-variant' as the value = project box flow
        self.browser.cookies_to_set = [
            {
                'name': 'seen_cookie_prompt',
                'value': 'yes',
                "path": "/",
            },
            {
                'name': 'force_optimizely',
                'value': 'add_wet_food_experiment_v3_feature_test:default,wet_food_selection_flow_test:b-variant,'
                         'new_account_onboarding_benefits_modal_test:default',

                'path': '/'
            },

        ]

        self.browser.cookies_to_set_pb = [
            {
                'name': 'seen_cookie_prompt',
                'value': 'yes',
                "path": "/",
            },
            {
                'name': 'force_optimizely',
                'value': 'price_page_redesign_v3_feature_test:default,'
                         'box_4_recommend_feeding_plan_feature_test:default,'
                         'box_4_essentials_card_update_feature_test:default,'
                         'new_account_onboarding_benefits_modal_test:default',
            }
        ]

    def select_country(self, country):
        return self.select_by_text("#country", country)

    def country_select_login(self, country):
        country_id = "gb"
        if country == "France": country_id = "fr"
        if country == "Deutschland": country_id = "de"
        if country == "Netherlands": country_id = "nl"
        if country == "Belgium": country_id = "be"
        if country == "Ireland": country_id = "ie"
        if country == "Austria": country_id = "at"
        if country == "Sweden": country_id = "se"
        if country == "Denmark": country_id = "de"
        self.goto(f"/{country_id}/signin")

    def country_select_(self, country):
        time.sleep(1)
        country_other_links = Select(self.find_xpath("//*[@id='other-links-top']/div[2]/select"))
        time.sleep(1)
        country_other_links.select_by_visible_text(country)

    def warning_close_cookie(self):
        time.sleep(7)

        if self.find(
                '#iubenda-cs-banner > div > div > div > div.iubenda-cs-opt-group > div.iubenda-cs-opt-group-consent > '
                'button'):
            self.click_element_(
                '#iubenda-cs-banner > div > div > div > div.iubenda-cs-opt-group > div.iubenda-cs-opt-group-consent > '
                'button')
        else:
            pass

    locator_dictionary = {
        "dismiss_verify": (By.XPATH, '//label[@class="ctp-checkbox-label"]//span[@class="mark"]'),
        "try_now": (By.XPATH, '//*[@class="btn btn-primary hide-logged-in"]'),
        "country": (By.CSS_SELECTOR, "select#country"),
        "login_country": (By.CSS_SELECTOR, "select#country-selector"),
        "country_submit": (By.CSS_SELECTOR, ".btn.btn-primary"),
        "country_selector": (By.TAG_NAME, "#select"),
        "raf_hero": (By.CSS_SELECTOR, "#hero-text"),
        "try_now_raf_page": (By.XPATH, '//*[@class="btn btn-primary hide-logged-in"]'),
        "country_banner_close": (By.XPATH, "//*[@class='banner-close']"),
        "store_info_link": (By.XPATH, "//*[@name='country-selector']"),
        "gb_country_radio": (By.XPATH, "//*[@for='radio-gb']"),
        "fr_country_radio": (By.XPATH, "//*[@for='radio-fr']"),
        "de_country_radio": (By.XPATH, "//*[@for='radio-de']"),
        "nl_country_radio": (By.XPATH, "//*[@for='radio-nl']"),
        "confirm_country": (By.XPATH, "//*[@id='delivery-country-confirm']"),
    }
