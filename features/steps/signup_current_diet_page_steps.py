from behave import when, use_step_matcher
from features.page_objects.current_diet_page import CurrentDietPage

use_step_matcher("re")


@when("Current diet select dry and wet food")
def _(context):
    current = CurrentDietPage(context)
    current_form = current.current_diet_form
    current.current_dryfood.click()
    current.current_drywet.click()
    current_form.submit()


@when("Current diet dry and wet food international")
def _(context):
    current = CurrentDietPage(context)
    current.current_dryfood.click()
    current.current_drywet.click()
    current.diet_next.click()


@when("Current diet dry food international")
def _(context):
    current = CurrentDietPage(context)
    current.current_dryfood.click()
    current.diet_next.click()


@when("Current diet dry food")
def _(context):
    current = CurrentDietPage(context)
    current_form = current.current_diet_form
    current.current_dryfood.click()
    current_form.submit()


@when("Current diet select dry wet food and treats other food")
def _(context):
    current = CurrentDietPage(context)
    current_form = current.current_diet_form
    current.current_dryfood.click()
    current.current_drywet.click()
    current.current_otherfood.click()
    current_form.submit()
