from behave import when, then, use_step_matcher
import time
from features.page_objects.current_food_page import CurrentFoodPage

use_step_matcher("re")


@when("Current food select no brand")
def _(context):
    current_food = CurrentFoodPage(context)
    current_food_form = current_food.current_food_form
    current_food.no_dryfood_brand.click()
    current_food_form.submit()


@when("Select flavour anything")
def _(context):
    current_flavour = CurrentFoodPage(context)
    flavours_form = current_flavour.flavours_form
    time.sleep(5)
    current_flavour.flavours_anything.click()
    flavours_form.submit()


@when("Select fish flavour")
def _(context):
    current_flavour = CurrentFoodPage(context)
    flavours_form = current_flavour.flavours_form
    current_flavour.flavours_fish.click()
    flavours_form.submit()


@when("Select lamb flavour")
def _(context):
    current_flavour = CurrentFoodPage(context)
    flavours_form = current_flavour.flavours_form
    current_flavour.flavours_lamb.click()
    flavours_form.submit()


@when('Current food selected wet "(.*)" austria')
def _(context, _wet):
    current_food = CurrentFoodPage(context)
    current_food_form = current_food.current_food_form
    current_food.current_wet_germany.click()
    current_food_form.submit()


@when('Current food selected wet "(.*)"')
def _(context, _wet):
    current_food = CurrentFoodPage(context)
    current_food_form = current_food.current_food_form
    current_food.no_dryfood_brand.click()
    current_food.scroll_to_bottom_of_page()
    if _wet == "Mini can (156g)":
        current_food.current_wet.click()
    if _wet == "Mini conserve (156g)":
        current_food.current_wet_france.click()
    if _wet == "Kleine Dose (156g)":
        current_food.current_wet_germany.click()
    time.sleep(5)
    current_food_form.submit()


@when('Current food no dry selected wet "(.*)"')
def _(context, wet_):
    current_food = CurrentFoodPage(context)
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
    time.sleep(5)
    current_food_form.submit()


@when('Current food dry "(.*)" selected wet "(.*)"')
def _(context, drybrand, wet):
    current_food = CurrentFoodPage(context)
    current_food_form = current_food.current_food_form
    current_food.no_dryfood_brand.click()
    current_food.scroll_to_bottom_of_page()
    if wet == "Mini can (156g)":
        current_food.current_wet.click()
    if wet == "Mini conserve (156g)":
        current_food.current_wet_france.click()
    if wet == "Kleine Dose (156g)":
        current_food.current_wet_germany.click()
    time.sleep(5)
    current_food_form.submit()


@when('Current food selected wet food "(.*)" international for "(.*)"')
def _(context, _wet, lang):
    current_food = CurrentFoodPage(context)
    if lang == "Netherlands":
        current_food.no_dryfood_brand.click()
    current_food_form = current_food.current_food_form
    if _wet == "Mini can (156g)":
        current_food.current_wet.click()
    time.sleep(5)
    current_food_form.submit()


@when("Select textures gravy")
def _(context):
    current_food = CurrentFoodPage(context)
    textures_form = current_food.textures_form
    current_food.scroll_to_bottom_of_page()
    textures_form.submit()


@when('Current food no dry selected wet "(.*)" international')
def _(context, wet_size):
    current_food = CurrentFoodPage(context)
    current_food_form = current_food.current_food_form
    if wet_size == "Mini can (156g)":
        current_food.current_wet.click()
    if wet_size == "Kleine Dose (156g)":
        current_food.current_wet_germany.click()
    time.sleep(5)
    current_food_form.submit()


@then('Error message with "(.*)" displayed on current food step')
def _(context, error):
    current_food = CurrentFoodPage(context)
    notification = current_food.error_notification

    assert error in notification.text
