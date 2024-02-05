from behave import when, then, use_step_matcher
import time
from features.page_objects.navigation_page import NavigationPage
from features.page_objects.pricing_page import PricingPage
from features.page_objects.email_page import EmailPage


use_step_matcher("re")


@when('Add another dog from pricing page "(.*)"')
def _(context, country):
    pricing = PricingPage(context)
    time.sleep(20)

    navigation = NavigationPage(context)
    if country in ["Germany", "France", "Austria", "Ireland", "Netherlands", "Denmark", "Sweden", "Belgium"]:
        pricing.manage_dogs.click()
    time.sleep(10)
    navigation.pets_another_dog.click()


@when("Add another dog from pricing page")
def _(context):
    pricing = PricingPage(context)
    time.sleep(30)
    pricing.manage_dogs.click()
    navigation = NavigationPage(context)
    time.sleep(10)
    navigation.pets_another_dog.click()


@when("Navigate to Home logo")
def _(context):
    navigation = NavigationPage(context)
    time.sleep(10)
    navigation.home_logo.click()
    time.sleep(5)


@when('can Continue signup')
def _(context):
    nav = NavigationPage(context)
    time.sleep(10)
    nav.continue_sign.click()


@then('can continue signup for uk "(.*)"')
def _(context, dog_):
    nav = NavigationPage(context)
    # dog = MydogPage(context)
    time.sleep(10)
    nav.continue_sign.click()
    email = EmailPage(context)
    time.sleep(15)
    ready = email.food_ready_uk
    assert ready.text == dog_
    time.sleep(5)


@then('can Continue signup "(.*)"')
def _(context, dog_):
    nav = NavigationPage(context)
    time.sleep(10)
    nav.continue_sign.click()
    email = EmailPage(context)
    time.sleep(10)
    ready = email.food_ready
    assert ready.text == dog_
    time.sleep(5)


@when("Add another dog from navigation page")
def _(context):
    navigation = NavigationPage(context)
    time.sleep(10)
    navigation.pets_another_dog.click()
