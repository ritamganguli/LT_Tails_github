import time
from behave import *
from selenium.webdriver import Keys
from features.page_objects.activity_page import ActivityPage
from features.page_objects.breed_page import BreedPage
from features.page_objects.checkout_address_page import CheckoutAddressPage
from features.page_objects.current_diet_page import CurrentDietPage
from features.page_objects.current_food_page import CurrentFoodPage
from features.page_objects.email_page import EmailPage
from features.page_objects.health_Ingredients_page import HealthIngredientsPage
from features.page_objects.home_page import HomePage
from features.page_objects.motivation_page import MotivationPage
from features.page_objects.mydog_page import MydogPage
from features.page_objects.accessibility_page import AccessibilityPage
from features.page_objects.pricing_page import PricingPage
from features.page_objects.project_box_pages import ProjectBoxPages
from features.page_objects.weight_page import WeightPage

use_step_matcher("re")


@given('on homepage and "(.*)" country conduct Accessibility audit')
def _(context, country):
    home_page = HomePage(context)
    accessibility_page = AccessibilityPage(context)

    home_page.goto("/")

    for cookie in context.browser.cookies_to_set:
        context.browser.add_cookie(cookie)

    time.sleep(2)
    home_page.try_now.click()
    time.sleep(1)
    home_page.country.click()
    time.sleep(15)
    home_page.select_country(country)

    accessibility_page.perform_accessibility_audit_first_page(context)

    submit = home_page.country_submit
    assert submit.is_enabled()
    submit.click()


@when(
    'Add "(.*)" information age "(.*)" years "(.*)" months male neutered purebreed'
    ' "(.*)" conduct Accessibility audit'
)
def _(context, dogn, yr, mth, pure_breed_):
    dog = MydogPage(context)
    accessibility_page = AccessibilityPage(context)

    accessibility_page.perform_accessibility_audit_other_page(context)
    time.sleep(5)
    dog_form = dog.dog_form
    dog.name_input.send_keys(dogn)
    dog.years_input.send_keys(yr)
    dog.months_input.send_keys(mth)
    dog.male_input.click()
    dog.neutered_yes.click()
    dog_form.submit()

    accessibility_page.perform_accessibility_audit_other_page(context)

    breed = BreedPage(context)
    breed_form = breed.breed_form
    breed.purebreed_input.click()
    time.sleep(2)
    breed.crossbreed_input.click()
    breed.purebreed_input.click()
    time.sleep(7)
    breed.breed_search.send_keys(pure_breed_)

    time.sleep(5)
    breed.breed_search.send_keys(Keys.DOWN)

    accessibility_page.perform_accessibility_audit_other_page(context)

    breed_form.submit()


@when("Select gain weight motivation for dog food conduct Accessibility audit")
def _(context):
    motivation_page = MotivationPage(context)
    accessibility_page = AccessibilityPage(context)

    accessibility_page.perform_accessibility_audit_other_page(context)
    motivation = motivation_page.motivation_form
    motivation_page.gain_weight.click()
    motivation.submit()

    accessibility_page.perform_accessibility_audit_other_page(context)
    motivation_info = motivation_page.motivation_info_form
    motivation_info.submit()


@when('Status no working dog weight "(.*)" conduct Accessibility audit')
def _(context, number):
    weight = WeightPage(context)
    accessibility_page = AccessibilityPage(context)

    accessibility_page.perform_accessibility_audit_other_page(context)
    weight_form = weight.weight_form
    weight.weight_input.send_keys(number)
    time.sleep(7)
    weight.gain_little_weight.click()
    weight_form.submit()

    accessibility_page.perform_accessibility_audit_other_page(context)
    underweight_info = weight.underweight_info_form
    underweight_info.submit()

    accessibility_page.perform_accessibility_audit_other_page(context)
    activity_page = ActivityPage(context)
    activity_form = activity_page.activity_form
    activity_form.submit()


@when("Health Ingredients no issues UK conduct Accessibility audit")
def _(context):
    health_ingredients = HealthIngredientsPage(context)
    accessibility_page = AccessibilityPage(context)

    accessibility_page.perform_accessibility_audit_other_page(context)
    health = health_ingredients.health_form
    time.sleep(10)
    health.submit()

    accessibility_page.perform_accessibility_audit_other_page(context)
    exclusions = health_ingredients.exclusions_form_uk
    health_ingredients.no_exclusions_uk.click()
    exclusions.submit()


@when("Current diet select dry and wet food conduct Accessibility audit")
def _(context):
    current = CurrentDietPage(context)
    accessibility_page = AccessibilityPage(context)

    accessibility_page.perform_accessibility_audit_other_page(context)
    current_form = current.current_diet_form
    current.current_dryfood.click()
    current.current_drywet.click()

    accessibility_page.perform_accessibility_audit_other_page(context)

    current_form.submit()


@when('Current food no dry selected wet "(.*)" conduct Accessibility audit')
def _(context, wet_):
    current_food = CurrentFoodPage(context)
    accessibility_page = AccessibilityPage(context)

    accessibility_page.perform_accessibility_audit_other_page(context)
    current_food_form = current_food.current_food_form
    current_food.no_dryfood_brand.click()
    current_food.scroll_to_bottom_of_page()
    if wet_ == "Mini can (156g)":
        current_food.current_wet.click()
    if wet_ == "Giant can (1200g)":
        current_food.large_wet_portion.click()
    if wet_ == "Mini conserve (156g)":
        current_food.current_wet_france.click()
    if wet_ == "Kleine Dose (156g)":
        current_food.current_wet_germany.click()
    time.sleep(10)
    accessibility_page.perform_accessibility_audit_other_page(context)
    current_food_form.submit()


@when("Select flavour anything conduct Accessibility audit")
def _(context):
    current_flavour = CurrentFoodPage(context)
    accessibility_page = AccessibilityPage(context)

    accessibility_page.perform_accessibility_audit_other_page(context)
    flavours_form = current_flavour.flavours_form
    current_flavour.flavours_anything.click()
    flavours_form.submit()


@when("Complete email page conduct Accessibility audit")
def _(context):
    email = EmailPage(context)
    accessibility_page = AccessibilityPage(context)

    time.sleep(20)
    accessibility_page.perform_accessibility_audit_other_page(context)

    email_form = email.email_form

    email.create_random_email()
    time.sleep(2)
    email.opt_in_no.click()
    email.opt_in_yes.click()
    email.opt_in_no.click()
    email.scroll_to_bottom_of_page()

    time.sleep(7)
    accessibility_page.perform_accessibility_audit_other_page(context)
    email_form.submit()
    # time.sleep(35)


@when('select dry and wet food Project Box in "(.*)" conduct accessibility audit')
def _(context, country_for):
    # land on core diet page but go through to wet food link first
    box_page = ProjectBoxPages(context)
    accessibility_page = AccessibilityPage(context)

    time.sleep(35)
    box_page.see_wet_food.click()
    time.sleep(5)
    wet_page_header = box_page.wet_page_header
    if country_for in ("United Kingdom", "Belgium", "Denmark", "Ireland", "Sweden"):
        assert "wet food selection" in wet_page_header.text
    if country_for in ("Germany", "Austria"):
        assert "Die Nassfutter-Auswahl" in wet_page_header.text
    accessibility_page.perform_accessibility_audit_other_page(context)
    time.sleep(25)
    # back to core diet page
    box_page.choose_this_selection_button.click()
    time.sleep(20)
    core_diet_header = box_page.core_diet_header
    if country_for in ("United Kingdom", "Belgium", "Denmark", "Ireland", "Sweden"):
        assert "unique feeding plan" in core_diet_header.text
    if country_for in ("Germany", "Austria"):
        assert "individuelle Ernährungsplan" in core_diet_header.text
    accessibility_page.perform_accessibility_audit_other_page(context)

    # core diet to treats via CTA
    box_page.add_to_box_button.click()
    time.sleep(25)

    essentials_page_header = box_page.essentials_page_header
    if country_for in ("United Kingdom", "Belgium", "Denmark", "Ireland", "Sweden"):
        assert "Handpicked" in essentials_page_header.text
    if country_for in ("Germany", "Austria"):
        assert "ausgewählt" in essentials_page_header.text
    if country_for == "Netherlands":
        assert "Handmatig geselecteerd" in essentials_page_header.text
    accessibility_page.perform_accessibility_audit_other_page(context)


@when('Select no treats Project Box conduct Accessibility audit')
def _(context):
    treats_page = ProjectBoxPages(context)
    accessibility_page = AccessibilityPage(context)

    treats_page.scroll_up_page()
    time.sleep(1)
    accessibility_page.perform_accessibility_audit_other_page(context)
    treats_page.go_to_box_button.click()
    time.sleep(10)


@when("Pricing continue with card conduct Accessibility audit")
def _(context):
    pricing = PricingPage(context)
    accessibility_page = AccessibilityPage(context)
    time.sleep(20)
    accessibility_page.perform_accessibility_audit_other_page(context)
    pricing.card_option.click()
    pricing.submit_pricing.click()


@then('Checkout with remote postcode "(.*)" conduct Accessibility audit')
def _(context, postc_remote):
    address = CheckoutAddressPage(context)
    accessibility_page = AccessibilityPage(context)
    accessibility_page.perform_accessibility_audit_other_page(context)
    address.first_name.send_keys("qatest")
    address.last_name.send_keys("qatest")
    address.password.send_keys("password1234")
    address.opt_out_phone.click()
    address.opt_out_text.click()
    time.sleep(2)
    address.address_next.click()

    address.search_postcode.send_keys(postc_remote)
    address.postcode_lookup.click()
    address.opt_in_email.click()
    time.sleep(20)
    address.remote_address_select()
    time.sleep(10)
    address.get_dates.click()
    time.sleep(7)
    accessibility_page.perform_accessibility_audit_other_page(context)
    address.next.click()


@when('navigate into signup flow in "(.*)" country prod conduct Accessibility audit')
def _(context, country):
    home_page = HomePage(context)
    accessibility_page = AccessibilityPage(context)
    time.sleep(5)
    home_page.warning_close_cookie()
    accessibility_page.perform_accessibility_audit_other_page(context)
    time.sleep(5)
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   home_page.try_now)
    home_page.try_now.click()
