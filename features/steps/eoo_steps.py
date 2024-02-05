import time
from behave import *

from features.page_objects.treatments_page import TreatmentPage
from features.page_objects.dashboard_page import DashboardPage
from features.page_objects.deliveries_page import DeliveriesPage
from features.page_objects.profile_loggedin_page import ProfilePage
from features.page_objects.weight_confirm import WeightConfirmPage

use_step_matcher("re")


@when('Navigates to Treatment page and subscribes for FWT & validates the confirmation "(.*)"')
def _(context, message):
    dashboard_page = DashboardPage(context)
    treatment_page = TreatmentPage(context)
    time.sleep(5)

    dashboard_page.hamburger_menu.click()
    time.sleep(5)

    dashboard_page.treatment_page.click()
    time.sleep(5)
    context.browser.execute_script("window.scrollBy(0,300);")
    treatment_page.fwt_subscribe.click()
    time.sleep(5)

    fwt_subscription_confirmation = treatment_page.fwt_subscription_confirmation
    assert message in fwt_subscription_confirmation.text


@When('Validates the FWT subscription header "(.*)" in Delivery page')
def _(context, header):
    deliveries_page = DeliveriesPage(context)
    dashboard_page = DashboardPage(context)
    time.sleep(10)

    dashboard_page.hamburger_menu.click()
    dashboard_page.deliveries_page_select.click()

    fwt_header = deliveries_page.fwt_delivery_header
    assert fwt_header.text == header


@When('Validates the FWT subscription text "(.*)" in View Delivery Details page')
def _(context, text):
    deliveries_page = DeliveriesPage(context)
    time.sleep(15)

    deliveries_page.view_treatment_delivery_button.click()
    confirm_fwt_next_delivery = deliveries_page.confirm_fwt_next_delivery
    assert confirm_fwt_next_delivery.text == text


@When('User unsubscribes from the treatment')
def _(context):
    dashboard_page = DashboardPage(context)
    treatment_page = TreatmentPage(context)

    dashboard_page.hamburger_menu.click()
    time.sleep(5)

    dashboard_page.treatment_page.click()
    time.sleep(5)

    treatment_page.fwt_unsubscribe.click()


@Then('Validates the confirmation message "(.*)"')
def _(context, message):
    treatment_page = TreatmentPage(context)

    fwt_unsubscription_confirmation = treatment_page.fwt_unsubscription_confirmation
    assert message in fwt_unsubscription_confirmation.text


@When('Update weight and confirm')
def _(context):
    profile_page = ProfilePage(context)
    weight_confirm = WeightConfirmPage(context)

    time.sleep(10)
    context.browser.execute_script("window.scrollBy(0,500);")
    profile_page.update_weight.click()

    assert profile_page.weight_header.is_displayed()

    profile_page.weight_input.clear()
    profile_page.weight_input.send_keys(22)
    profile_page.next_button.click()

    weight_confirm.weight_confirm.click()

    assert profile_page.condition_header.is_displayed()

    profile_page.next_button.click()


@When('Update weight less than 2kg')
def _(context):
    profile_page = ProfilePage(context)
    weight_confirm = WeightConfirmPage(context)

    profile_page.update_weight.click()
    context.browser.execute_script("window.scrollBy(0,300);")
    assert profile_page.weight_header.is_displayed()

    profile_page.weight_input.clear()
    profile_page.weight_input.send_keys(1.98)
    profile_page.next_button.click()

    weight_confirm.weight_confirm.click()

    assert profile_page.condition_header.is_displayed()

    profile_page.next_button.click()


@Then('Confirm feeding plan changes and verify price change text "(.*)"')
def _(context, message):
    profile_page = ProfilePage(context)

    assert profile_page.feeding_plan_header.text == "Confirm new feeding plan"

    assert message in profile_page.price_change.text

    time.sleep(2)

    profile_page.confirm_button.click()


@Then('Confirm feeding plan changes and verify ineligible message "(.*)"')
def _(context, message):
    profile_page = ProfilePage(context)
    time.sleep(10)
    assert profile_page.feeding_plan_header.text == "Confirm new feeding plan"
    context.browser.execute_script("window.scrollBy(0,300);")
    assert message in profile_page.fwt_not_eligible_message.text

    # profile_page.scroll_down_page()
    time.sleep(2)
    context.browser.execute_script("window.scrollBy(0,500);")
    profile_page.confirm_button.click()
