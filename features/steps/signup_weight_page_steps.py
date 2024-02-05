from behave import when, then, use_step_matcher
import time
from features.page_objects.weight_page import WeightPage
from features.page_objects.activity_page import ActivityPage
from features.page_objects.health_Ingredients_page import HealthIngredientsPage
use_step_matcher("re")


@when('Status no working dog weight estimate')
def _(context):
    weight = WeightPage(context)
    weight_form = weight.weight_form
    weight.estimate_weight_link.click()
    time.sleep(2)
    weight.estimate_weight_button.click()
    weight_form.submit()

    activity_page = ActivityPage(context)
    activity_form = activity_page.activity_form
    activity_form.submit()


@when('Status no working dog weight "(.*)"')
def _(context, number):
    weight = WeightPage(context)
    weight_form = weight.weight_form
    weight.weight_input.send_keys(number)
    time.sleep(7)
    weight.gain_little_weight.click()
    weight_form.submit()
    time.sleep(7)
    underweight_info = weight.underweight_info_form
    underweight_info.submit()
    time.sleep(7)
    activity_page = ActivityPage(context)
    activity_form = activity_page.activity_form
    activity_form.submit()


@when('Status no working puppy weight "(.*)"')
def _(context, weight="6"):
    weight = WeightPage(context)
    weight_form = weight.weight_form
    weight.weight_input.send_keys(6)
    weight.gain_little_weight.click()
    weight_form.submit()
    time.sleep(2)
    underweight_info = weight.underweight_info_form
    underweight_info.submit()

    activity_page = ActivityPage(context)
    activity_page.puppy_route()
    health_ingredients = HealthIngredientsPage(context)
    time.sleep(5)
    puppy_health = health_ingredients.puppy_health_form
    puppy_health.submit()


@when('Status no working dog weight "(.*)" just right weight')
def _(context, number):
    weight = WeightPage(context)
    weight_form = weight.weight_form
    time.sleep(10)
    weight.weight_input.send_keys(number)
    weight.maintain_weight.click()
    weight_form.submit()


@when('Status no working dog weight "(.*)" just right weight and activity')
def _(context, number):
    weight = WeightPage(context)
    weight_form = weight.weight_form
    weight.weight_input.send_keys(number)
    weight.maintain_weight.click()
    weight_form.submit()
    activity_page = ActivityPage(context)
    activity_form = activity_page.activity_form
    activity_form.submit()


@then('Error message with "(.*)" is displayed on the weight step')
def _(context, error):
    weight = WeightPage(context)
    notification = weight.weight_error_notification

    assert error in notification.text
