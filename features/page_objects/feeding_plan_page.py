from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class FeedingPlanPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def claims_health(self, claim):
        return self.find_xpath(f"//b[contains(text(), '{claim}')]")

    locator_dictionary = {
        "feeding_plan": (By.CSS_SELECTOR, "#signup-feeding-plan"),
        "next_feeding_plan": (By.CSS_SELECTOR, "#submit-pricing-details"),
        "next_feeding_plan_nl": (By.CSS_SELECTOR, "#submit-pricing-details"),
        "designed_support": (By.XPATH, "//p[strong = 'Designed to support:']"),
        "fr_designed_support": (By.XPATH, "//p[strong]"),
        "de_designed_support": (By.XPATH, "//p[strong]"),
        "nl_designed_support": (By.XPATH, "//p[strong]"),
        "eng_designed_support": (By.XPATH, "//p[strong]"),
        "contains_no": (By.XPATH, "//*[@id='signup-feeding-plan'][contains(text(),'')]"),
        "claims": (By.XPATH, "//*[@id='__layout']/div/div/div[2]/div[1]/div[2]/div[2]"),
        "fr_contains_no": (By.XPATH, "//p[3][strong]"),
        "ge_contains_no": (By.XPATH, "//p[3][strong]"),
        "nl_contains_no": (By.XPATH, "//p[3][strong]"),
        "nl_contains_no_ingredients": (By.XPATH, "//p[strong]"),
        "fr_contains_no_ingredients": (By.XPATH, "//p[strong]"),
        "eng_contains_no": (By.XPATH, "//p[strong]"),
        "gr_contains_no": (By.XPATH, "//p[strong = 'Ohne:']"),
        "another_dog": (By.LINK_TEXT, "Add another dog"),
        "fr_another_dog": (
            By.XPATH,
            "//*[@id='signup-feeding-plan']/div[6]/a/"
            "span[contains(text(),'Ajouter un autre chien')]",

        ),
        "de_another_dog": (
            By.CSS_SELECTOR,
            "#signup-feeding-plan > div.footer-cta > a > span",
        ),
        "nl_another_dog": (By.XPATH,
                           "//*[@id='signup-feeding-plan']/div[6]/a/"
                           "span[contains(text(),'Een andere hond toevoegen')]",

                           ),
        "recipe_form": (
            By.CSS_SELECTOR,
            "form flow-my-dog dry-recipe-choice tails-view "
            "tails-view-dry-recipe-choice",
        ),
        "paypal_button": (By.XPATH, "//*[@label='paypal-radio']"),
        "feeding_plan_summary": (By.XPATH, "//*[@class='first trial']"),
    }
