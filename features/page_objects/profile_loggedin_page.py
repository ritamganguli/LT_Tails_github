from selenium.webdriver.common.by import By

from .base_page_object import BasePage


class ProfilePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser),

    locator_dictionary = {

        "weight_condition": (By.XPATH, "//div[@class='name']//strong[contains(text(),'Weight & condition')]"),
        "update_weight": (By.XPATH, "//a[contains(@href,'weight')]"),
        "weight_header": (By.XPATH, "//h1[normalize-space()='Update weight']"),
        "weight_input": (By.CSS_SELECTOR, "#weight"),
        "condition_header": (By.XPATH, "//h1[normalize-space()='Update condition']"),
        "next_button": (By.XPATH, "//*[@class='btn btn-primary next']"),
        "feeding_plan_header": (By.XPATH, "//h1[normalize-space()='Confirm new feeding plan']"),
        "confirm_button": (By.XPATH, "//button[@type='submit'][contains(text(),'Confirm')]"),
        "profile_notification": (By.XPATH, "//*[@class='notification-content ']"),
        "update_condition": (By.XPATH, "//a[contains(@href,'health-issues')]"),
        "joints": (By.XPATH, "//label[@for='health_issue_1']"),
        "skin_coat": (By.XPATH, "//label[@for='health_issue_2']"),
        "digestion": (By.XPATH, "//label[@for='health_issue_3']"),
        "pancreatitis": (By.XPATH, "//label[@for='health_issue_4']"),
        "continue_button": (By.XPATH, "//*/input[@value = 'Continue']"),
        "pancreatitis_continue": (By.XPATH, "//*[@type='submit']"),
        "suitability_notification": (By.XPATH, "//*[@class='details']/span[contains(text(),'Some recipes')]"),
        "add_exclusion": (By.XPATH, "//a[contains(@href,'exclusions')]"),
        "exclusion_header": (By.XPATH, "//p[contains(text(),'Select the ingredients')]"),
        "chicken_exclusion": (By.XPATH, "//*[@for='allergen_id_3']"),
        "beef_exclusion": (By.XPATH, "//*[@for='allergen_id_2']"),
        "lamb_exclusion": (By.XPATH, "//*[@for='allergen_id_8']"),
        "fish_exclusion": (By.XPATH, "//*[@for='allergen_id_5']"),
        "wheat_exclusion": (By.XPATH, "//*[@for='allergen_id_1']"),
        "grain_exclusion": (By.XPATH, "//*[@for='allergen_id_10']"),
        "maize_exclusion": (By.XPATH, "//*[@for='allergen_id_9']"),
        "soya_exclusion": (By.XPATH, "//*[@for='allergen_id_4']"),
        "egg_exclusion": (By.XPATH, "//*[@for='allergen_id_7']"),
        "hypoallergenic_exclusion": (By.XPATH, "//*[@for='allergen-category-1']"),
        "view_feeding_plan_cta": (By.CSS_SELECTOR, ".profile .btn.btn-primary"),
        "price_change": (By.XPATH, "//*[@class='recurring-cost-info']"),
        "fwt_not_eligible_message": (By.XPATH, "//*[@class='no-more-eligible-warning']"),
        "update_activity": (By.XPATH, "//a[contains(@href,'exercise')]"),
        "update_textures": (By.XPATH, "//a[contains(@href,'textures')]"),
        "how_it_works_link": (By.XPATH, "//*[@href='/gb/how-it-works']")


    }
