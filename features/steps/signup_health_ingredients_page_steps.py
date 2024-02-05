import time
from behave import when, use_step_matcher
from features.page_objects.health_Ingredients_page import HealthIngredientsPage

use_step_matcher("re")


@when(
    "Health issues none and ingredients excluded wheat beef chicken soya fish dairy egg"
)
def _(context):
    health_ingredients = HealthIngredientsPage(context)
    health = health_ingredients.health_form
    time.sleep(15)
    health.submit()

    exclusions = health_ingredients.exclusions_form
    health_ingredients.yes_exclusions.click()

    health_ingredients.beef.click()
    health_ingredients.chicken.click()
    health_ingredients.dairy.click()
    health_ingredients.egg.click()
    health_ingredients.fish.click()
    health_ingredients.grain.click()
    health_ingredients.lamb.click()
    health_ingredients.maize.click()
    health_ingredients.soya.click()
    health_ingredients.wheat.click()
    exclusions.submit()


@when('Health issues "(.*)" selected lamb and wheat')
def _(context, lang):
    health_ingredients = HealthIngredientsPage(context)
    if lang == "English":
        exclusions = health_ingredients.exclusions_form_uk
        health_ingredients.yes_exclusions_uk.click()
        health_ingredients.lamb_uk.click()
        health_ingredients.wheat_uk.click()

        exclusions.submit()

    if lang == "German":
        exclusions = health_ingredients.exclusions_form
        health_ingredients.yes_exclusions.click()
        health_ingredients.lamb.click()
        health_ingredients.wheat.click()

        exclusions.submit()

    if lang == "France":
        exclusions = health_ingredients.exclusions_form
        health_ingredients.yes_exclusions.click()
        health_ingredients.lamb.click()
        health_ingredients.wheat.click()

        exclusions.submit()

    if lang == "Dutch":
        exclusions = health_ingredients.exclusions_form
        health_ingredients.yes_exclusions.click()
        health_ingredients.lamb.click()
        health_ingredients.wheat.click()

        exclusions.submit()
    if lang == "International":
        exclusions = health_ingredients.exclusions_form
        health_ingredients.yes_exclusions.click()
        health_ingredients.lamb.click()
        health_ingredients.wheat.click()
        exclusions.submit()


@when('health all issues Joints Skin and coat Digestion Pancreatitis in "(.*)"')
def _(context, country_for):
    health_ingredients = HealthIngredientsPage(context)
    health = health_ingredients.health_form
    time.sleep(10)
    # pancreatitis_info = health_ingredients.pancreatitis_info_box
    health_ingredients.joints.click()
    health_ingredients.skin_coat.click()
    health_ingredients.digestion.click()
    context.browser.execute_script("window.scrollBy(0,400);")
    health_ingredients.pancreatitis.click()
    pancreatitis_info = health_ingredients.pancreatitis_info_box

    if country_for in ("Germany", "Austria"):
        assert "es wurde mindestens ein Mal vom Tierarzt Pankreatitis diagnostiziert" in pancreatitis_info.text
    elif country_for == "France":
        assert "A déjà été atteint de pancréatite diagnostiquée par un vétérinaire" in pancreatitis_info.text
    elif country_for == "Netherlands":
        assert "heeft ten minste één acute episode van pancreatitis gehad, vastgesteld door een dierenarts" in pancreatitis_info.text
    else:
        assert "has had at least one veterinary diagnosed episode of pancreatitis" in pancreatitis_info.text

    health.submit()
    time.sleep(2)

    multi_condition_info = health_ingredients.multiple_condition_info
    multi_condition_info.submit()
    time.sleep(2)

    exclusions = health_ingredients.exclusions_form
    health_ingredients.no_exclusions_inter.click()
    exclusions.submit()


@when("Health Ingredients all health issues with hypoallergenic")
def _(context):
    health_ingredients = HealthIngredientsPage(context)
    health = health_ingredients.health_form
    health_ingredients.joints.click()
    health_ingredients.skin_coat.click()
    health_ingredients.digestion.click()
    context.browser.execute_script("window.scrollBy(0,400);")
    health_ingredients.pancreatitis.click()
    # health_ingredients.no_vet_pet_health_issues()
    health.submit()

    multi_condition_info = health_ingredients.multiple_condition_info
    multi_condition_info.submit()

    exclusions = health_ingredients.exclusions_form
    health_ingredients.yes_exclusions.click()
    health_ingredients.hypo.click()
    exclusions.submit()


@when("Health Ingredients no health issues with hypoallergenic UK")
def step_impl(context):
    health_ingredients = HealthIngredientsPage(context)
    health = health_ingredients.health_form
    health_ingredients.joints.click()
    health_ingredients.skin_coat.click()
    health_ingredients.digestion.click()
    context.browser.execute_script("window.scrollBy(0,400);")
    health_ingredients.pancreatitis.click()

    health.submit()

    multi_condition_info = health_ingredients.multiple_condition_info
    multi_condition_info.submit()

    exclusions = health_ingredients.exclusions_form_uk
    health_ingredients.yes_exclusions_uk.click()
    health_ingredients.hypo_uk.click()
    exclusions.submit()


@when("Health Ingredients no issues")
def _(context):
    health_ingredients = HealthIngredientsPage(context)
    health = health_ingredients.health_form
    time.sleep(7)
    health.submit()

    health_ingredients.no_exclusions_inter.click()
    health_ingredients.exclusions_next_inter.click()


@when("Health Ingredients no issues UK")
def _(context):
    health_ingredients = HealthIngredientsPage(context)
    health = health_ingredients.health_form
    time.sleep(10)
    health.submit()

    exclusions = health_ingredients.exclusions_form_uk
    health_ingredients.no_exclusions_uk.click()
    exclusions.submit()


@when("health all issues Joints Skin and coat Digestion Pancreatitis exclusions none UK")
def _(context):
    health_ingredients = HealthIngredientsPage(context)
    health = health_ingredients.health_form
    # time.sleep(10)
    health_ingredients.joints.click()
    health_ingredients.skin_coat.click()
    health_ingredients.digestion.click()
    context.browser.execute_script("window.scrollBy(0,400);")
    health_ingredients.pancreatitis.click()
    # health_ingredients.no_vet_pet_health_issues()

    health.submit()

    multi_condition_info = health_ingredients.multiple_condition_info
    multi_condition_info.submit()

    exclusions = health_ingredients.exclusions_form_uk
    health_ingredients.no_exclusions_uk.click()
    exclusions.submit()


@when("No health issues with hypoallergenic selected UK")
def _(context):
    health_ingredients = HealthIngredientsPage(context)
    health = health_ingredients.health_form
    time.sleep(10)
    health.submit()

    time.sleep(10)
    exclusions = health_ingredients.exclusions_form_uk
    health_ingredients.yes_exclusions_uk.click()
    health_ingredients.hypo_uk.click()
    exclusions.submit()


@when(
    "Health issues none and ingredients excluded wheat beef chicken soya fish dairy egg UK"
)
def _(context):
    health_ingredients = HealthIngredientsPage(context)
    health = health_ingredients.health_form
    time.sleep(10)
    health.submit()

    exclusions = health_ingredients.exclusions_form_uk
    health_ingredients.yes_exclusions_uk.click()

    health_ingredients.beef_uk.click()
    health_ingredients.chicken_uk.click()
    health_ingredients.dairy_uk.click()
    health_ingredients.egg_uk.click()
    health_ingredients.fish_uk.click()
    health_ingredients.grain_uk.click()
    health_ingredients.lamb_uk.click()
    health_ingredients.maize_uk.click()
    health_ingredients.soya_uk.click()
    health_ingredients.wheat_uk.click()
    exclusions.submit()


@when("Health issues skin and coat and ingredients excluded soya")
def _(context):
    health_ingredients = HealthIngredientsPage(context)
    health = health_ingredients.health_form
    health_ingredients.skin_coat_uk.click()
    health.submit()

    skin_coat_info = health_ingredients.skin_coat_info
    skin_coat_info.submit()

    exclusions = health_ingredients.exclusions_form_uk
    health_ingredients.yes_exclusions_uk.click()
    health_ingredients.yes_exclusions_uk.click()
    health_ingredients.soya_uk.click()
    exclusions.submit()


@when("Health issues none and ingredients excluded lamb")
def _(context):
    health_ingredients = HealthIngredientsPage(context)
    health = health_ingredients.health_form
    health.submit()
    exclusions = health_ingredients.exclusions_form_uk
    health_ingredients.yes_exclusions_uk.click()
    health_ingredients.lamb_uk.click()

    exclusions.submit()


@when("Health issues none and ingredients excluded lamb and fish")
def _(context):
    health_ingredients = HealthIngredientsPage(context)
    health = health_ingredients.health_form
    health.submit()
    exclusions = health_ingredients.exclusions_form_uk
    health_ingredients.yes_exclusions_uk.click()
    health_ingredients.lamb_uk.click()
    health_ingredients.fish_uk.click()
    exclusions.submit()


@when("Health issues none and ingredients excluded wheat")
def _(context):
    health_ingredients = HealthIngredientsPage(context)
    health = health_ingredients.health_form
    health.submit()
    exclusions = health_ingredients.exclusions_form_uk
    health_ingredients.yes_exclusions_uk.click()
    health_ingredients.wheat_uk.click()
    exclusions.submit()


@when(
    'Health issues none "(.*)" selected lamb and no chicken and egg option to excluded'
    " reset exclusions UK"
)
def _(context, content_lang):
    health_ingredient = HealthIngredientsPage(context)

    exclusions = health_ingredient.exclusions_form_uk
    health_ingredient.yes_exclusions_uk.click()
    health_ingredient.lamb_uk.click()
    health_ingredient.yes_exclusions_uk.click()
    health_ingredient.beef_uk.click()
    health_ingredient.dairy_uk.click()
    health_ingredient.soya_uk.click()
    health_ingredient.beef_uk.click()
    health_ingredient.dairy_uk.click()
    health_ingredient.soya_uk.click()
    health_ingredient.beef_uk.click()

    health_ingredient.wheat_uk.click()
    health_ingredient.wheat_uk.click()
    health_ingredient.beef_uk.click()

    exclusions.submit()
