import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from .base_page_object import BasePage


class MydogPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def age_puppy_set(self, mth):
        current_date = datetime.now()
        print('Current Date: ', current_date, file=sys.stderr)
        # Subtract months from current date
        n = int(mth)
        past_date = current_date - relativedelta(months=n)

        year_ = past_date.strftime("%Y")
        print("year:", year_, file=sys.stderr)

        month_ = past_date.strftime("X%m").replace('X0', 'X').replace('X', '')
        print("month:", month_, file=sys.stderr)

        day_ = past_date.strftime("X%d").replace('X0', 'X').replace('X', '')
        print("day:", day_, file=sys.stderr)

        days = Select(self.dob)
        days.select_by_visible_text(day_)
        months = Select(self.month)
        months.select_by_value(month_)
        years = Select(self.year)
        years.select_by_visible_text(year_)

    locator_dictionary = {
        "dog_form": (By.CSS_SELECTOR, "#form_basics"),
        "puppy_form": (By.CSS_SELECTOR, "#form_puppy_birthday"),
        "name_input": (By.CSS_SELECTOR, "#pet_name-pet_name"),
        "years_input": (By.CSS_SELECTOR, "#age-age_years"),
        "months_input": (By.CSS_SELECTOR, "#age-age_months"),
        "male_input": (By.XPATH, "//*[@id='sex-choice-male']"),
        "neutered_yes": (By.CSS_SELECTOR, "label[for=neutered-choice-yes]"),
        "female_input": (By.XPATH, "//*[@id='sex-choice-female']"),
        "neutered_no": (By.CSS_SELECTOR, "label[for=neutered-choice-no]"),
        "dob": (By.CSS_SELECTOR, "#dob_day"),
        "month": (By.CSS_SELECTOR, "#dob_month"),
        "year": (By.CSS_SELECTOR, "#dob_year"),
        "pregnant_form": (By.CSS_SELECTOR, "#form_pregnant"),
        "pregnant_yes": (By.XPATH, "//*[@id='pregnant-choice-yes']"),
        "pregnant_no": (By.XPATH, "//*[@id='pregnant-choice-no']"),
        "no_recipe": (By.XPATH, "//p[contains(text(),'At the moment, we ')]"),
        "german_no_recipe": (By.XPATH, "//p[contains(text(),'Im Moment stellen ')]"),
        "france_no_recipe": (
            By.XPATH,
            "//p[contains(text(),'Nous n’avons pas encore mis au point de recettes pour la grossesse')]",

        ),
        "netherlands_no_recipe": (
            By.XPATH, "//p[contains(text(),'We maken op dit moment geen unieke recepten voor drachtige honden')]"),
        "notification": (By.CSS_SELECTOR, "#notification neutral breed-alert show"),
        "no_recipe_dalmation": (
            By.XPATH,
            "//span[contains(text(),'We restrict protein and high purine ingredients for Dalmatians')]"
        ),
        "german_no_recipe_dalmation": (
            By.XPATH,
            '//*[@class="notification info breed-alert show"]',
        ),
        "france_no_recipe_dalmation": (
            By.XPATH,
            '//*[@class="notification info breed-alert show"]',
        ),
        "netherlands_no_recipe_dalmation": (
            By.XPATH,
            '//*[@class="notification info breed-alert show"][contains(text(),"")]',
        ),
        "promo_text": (By.XPATH, "//label[@for='tounge']//span[@class='offer-text']"),
        "my_dog_header": (By.XPATH, "//*[@data-testid='step-header']")
    }
