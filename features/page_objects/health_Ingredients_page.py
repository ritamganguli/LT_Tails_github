from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class HealthIngredientsPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
        )

    def no_vet_pet_health_issues(self):
        self.assert_element_is_not_visible("label[for=health_issue_3580726559]")

    locator_dictionary = {
        "health_form": (By.CSS_SELECTOR, "#form_health"),
        "joints": (By.CSS_SELECTOR, "label[for=health_issue_4020367548]"),
        "skin_coat": (By.CSS_SELECTOR, "label[for=health_issue_4192590813]"),
        "digestion": (By.CSS_SELECTOR, "label[for=health_issue_3408503550]"),
        "pancreatitis": (By.CSS_SELECTOR, "label[for=health_issue_3580726559]"),
        "pancreatitis_info_box": (By.XPATH, "//*[@id='health_issue_3580726559-checkbox']/div/p"),
        "exclusions_form": (By.CSS_SELECTOR, "#form_exclusions-preferences"),
        "exclusions_form_inter": (By.CSS_SELECTOR, "#form_exclusions"),
        "no_exclusions_inter": (By.XPATH, "//*[@id='exclusions-no']"),
        "exclusions_next_inter": (By.XPATH, "//*[@id='form_exclusions-preferences']/div[2]/div/button"),
        "no_exclusions": (By.CSS_SELECTOR, "label[for=exclusions-no]"),
        "yes_exclusions": (By.CSS_SELECTOR, "label[for=exclusions-yes]"),
        "multiple_condition_info": (By.CSS_SELECTOR, "#form_multiple-condition-info"),
        "skin_coat_info": (By.CSS_SELECTOR, "#form_skin-info"),
        "hypo": (By.CSS_SELECTOR, "label[for=hypo-allergen-category]"),
        "lamb": (By.CSS_SELECTOR, "label[for=exclusions_allergen_id_8]"),
        "beef": (By.CSS_SELECTOR, "label[for=exclusions_allergen_id_2]"),
        "soya": (By.CSS_SELECTOR, "label[for=exclusions_allergen_id_4]"),
        "dairy": (By.CSS_SELECTOR, "label[for=exclusions_allergen_id_6]"),
        "wheat": (By.CSS_SELECTOR, "label[for=exclusions_allergen_id_1]"),
        "chicken": (By.CSS_SELECTOR, "label[for=exclusions_allergen_id_3]"),
        "egg": (By.CSS_SELECTOR, "label[for=exclusions_allergen_id_7]"),
        "fish": (By.CSS_SELECTOR, "label[for=exclusions_allergen_id_5]"),
        "grain": (By.CSS_SELECTOR, "label[for=exclusions_allergen_id_10]"),
        "maize": (By.CSS_SELECTOR, "label[for=exclusions_allergen_id_9]"),
        "excl_reset": (By.CSS_SELECTOR, "#exclusion-reset"),
        "puppy_health_form": (By.CSS_SELECTOR, "#form_health"),
        "all_exclusions_available": (
            By.XPATH,
            "//span[@class='label'][contains(text()," ")]",
        ),

        # uk specific exclusions
        "exclusions_form_uk": (By.CSS_SELECTOR, "#form_exclusions-preferences"),
        "exclusions_form_uk_prod": (By.CSS_SELECTOR, "//*[@id='form_exclusions-preferences']/div[2]/div/button"),
        "no_exclusions_uk": (By.CSS_SELECTOR, "label[for=exclusions-no]"),
        "yes_exclusions_uk": (By.CSS_SELECTOR, "label[for=exclusions-yes]"),

        "hypo_uk": (By.CSS_SELECTOR, "label[for=hypo-allergen-category]"),
        "lamb_uk": (By.CSS_SELECTOR, "label[for=exclusions_allergen_id_8]"),
        "beef_uk": (By.CSS_SELECTOR, "label[for=exclusions_allergen_id_2]"),
        "soya_uk": (By.CSS_SELECTOR, "label[for=exclusions_allergen_id_4]"),
        "diary_uk": (By.CSS_SELECTOR, "label[for=exclusions_allergen_id_6]"),
        "wheat_uk": (By.CSS_SELECTOR, "label[for=exclusions_allergen_id_1]"),
        "chicken_uk": (By.CSS_SELECTOR, "label[for=exclusions_allergen_id_3]"),
        "egg_uk": (By.CSS_SELECTOR, "label[for=exclusions_allergen_id_7]"),
        "fish_uk": (By.CSS_SELECTOR, "label[for=exclusions_allergen_id_5]"),
        "grain_uk": (By.CSS_SELECTOR, "label[for=exclusions_allergen_id_10]"),
        "maize_uk": (By.CSS_SELECTOR, "label[for=exclusions_allergen_id_9]"),
        "skin_coat_uk": (By.XPATH, "//*[@class='health-choices']//span[contains(text(),'Skin and Coat')]")

    }
