from behave import when, then, use_step_matcher
import time

from selenium.webdriver import ActionChains, Keys
from features.page_objects.pricing_page import PricingPage
from features.page_objects.navigation_page import NavigationPage

use_step_matcher("re")


@then('Pricing and pets page with three dogs "(.*)"')
def _(context, third_):
    pricing = PricingPage(context)
    navigation = NavigationPage(context)
    time.sleep(10)

    pricing.manage_dogs.click()

    time.sleep(10)
    pets = navigation.three_dogs_profile
    assert third_ == pets.text


@then('Pricing and pets page german with three dogs "(.*)"')
def _(context, _third):
    pricing = PricingPage(context)
    pricing.scroll_to_bottom_of_page()
    time.sleep(10)
    element = pricing.manage_dogs
    actions = ActionChains(pricing.browser)
    actions.move_to_element(element).click_and_hold(element).perform()
    pricing.manage_dogs.click()
    navigation = NavigationPage(context)
    time.sleep(10)
    pets = navigation.three_dogs_profile
    assert _third == pets.text


@when('Pricing page with "(.*)"')
def _(context, _dental_dailies):
    pricing = PricingPage(context)

    time.sleep(5)
    pricing.scroll_down_page()
    pricing.scroll_down_page()
    time.sleep(5)
    assert _dental_dailies in pricing.dental_trial_pricing_page.text
    pricing.scroll_to_bottom_of_page()
    time.sleep(5)
    element = pricing.card_option
    actions = ActionChains(pricing.browser)
    actions.move_to_element(element).click_and_hold(element).perform()
    pricing.card_option.click()
    pricing.submit_pricing.click()


@then('pricing page with "(.*)"')
def _(context, _essential_product):
    pricing = PricingPage(context)
    actions = ActionChains(pricing.browser)

    time.sleep(10)
    pricing.scroll_down_page()
    pricing.scroll_down_page()
    time.sleep(5)
    assert _essential_product in pricing.trial_pricing_table.text
    pricing.scroll_to_bottom_of_page()
    time.sleep(5)
    actions.move_to_element(pricing.card_option).click(pricing.card_option).perform()
    pricing.submit_pricing.click()


@then('Pricing and pet page german for "(.*)"')
def _(context, two_):
    pricing = PricingPage(context)
    pricing.scroll_to_bottom_of_page()
    time.sleep(7)
    pricing.manage_dogs.click()
    navigation = NavigationPage(context)
    time.sleep(7)
    pets = navigation.two_dogs_profile
    assert two_ == pets.text


@then('Pricing and pet page for "(.*)"')
def _(context, two_):
    pricing = PricingPage(context)
    time.sleep(15)
    pricing.manage_dogs.click()
    time.sleep(7)


@when("Pricing continue with card")
def _(context):
    pricing = PricingPage(context)
    time.sleep(10)
    context.browser.execute_script("window.scrollBy(0,600);")
    pricing.card_option.click()
    pricing.submit_pricing.click()


@when("Pricing continue with ideal")
def _(context):
    pricing = PricingPage(context)
    nav = NavigationPage(context)

    # context.browser.execute_script("window.scrollBy(0,500);")
    # time.sleep(10)
    # element = pricing.ideal_option
    # actions = ActionChains(pricing.browser)
    # actions.move_to_element(element).click_and_hold(element).perform()

    time.sleep(20)
    context.browser.execute_script("window.scrollBy(0,1800);")
    # pricing.ideal_option.click()
    # pricing.check_if_on_treats_page()
    pricing.pricing_payment_option_ideal()
    pricing.pricing_payment_option_ideal()
    pricing.pricing_payment_option_ideal()
    # context.browser.execute_script("window.scrollBy(0,-1800);")
    # context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
    #                                pricing.standard_pricing_tab)
    nav.check_height_page_go_top_of_page()
    time.sleep(10)
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   pricing.standard_pricing_tab)
    pricing.standard_pricing_tab.click()
    pricing.standard_pricing_tab.send_keys(Keys.TAB * 2)

    actions = ActionChains(pricing.browser)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    # pricing.pricing_page_ideal_submit()
    # pricing.submit_pricing_ideal.click()
    time.sleep(2)


@when('Pricing continue with Paypal payment method "(.*)"')
def _(context, checkout_):
    PricingPage(context).select_paypal_payment_method(checkout_)


@then('Confirm "(.*)" displayed in price table')
def _(context, product_name):
    pricing = PricingPage(context)
    assert product_name in pricing.price_table.text
