import datetime
import sys

from behave import given, when, then, use_step_matcher

import time
from features.page_objects.dashboard_page import DashboardPage
from features.page_objects.deliveries_page import DeliveriesPage
from features.page_objects.frontyard import FrontyardPage
from features.page_objects.email_page import EmailPage
from features.data_seed.provider_state_seeds import *

use_step_matcher("re")


@when('Select deliveries page via menu confirm "(.*)" displays')
def _(context, delivery):
    deliveries_page = DeliveriesPage(context)
    dashboard_page = DashboardPage(context)

    dashboard_page.hamburger_menu.click()
    time.sleep(5)

    dashboard_page.deliveries_page_select.click()

    deliveries_header = deliveries_page.deliveries_header
    assert deliveries_header.text == delivery


@when('Select deliveries page and confirm "(.*)" displays')
def _(context, header):
    deliveries_page = DeliveriesPage(context)
    dashboard_page = DashboardPage(context)

    dashboard_page.hamburger_menu.click()
    dashboard_page.deliveries_page_select.click()

    deliveries_header = deliveries_page.deliveries_header
    assert deliveries_header.text == header


@when("View full delivery details")
def _(context):
    deliveries_page = DeliveriesPage(context)
    deliveries_page.view_delivery_button.click()


@then('Confirm dry food item "(.*)" displays on manage box page')
def _(context, message):
    deliveries_page = DeliveriesPage(context)
    assert deliveries_page.manage_my_box_dry_food_item.text == message


@then('Pause deliveries message "(.*)" on confirmation page is displayed')
def _(context, message):
    assert message in DeliveriesPage(context).pause_delivery_confirmation.text


@when("Navigates to manage my box page")
def _(context):
    deliveries_page = DeliveriesPage(context)
    dashboard_page = DashboardPage(context)
    time.sleep(6)
    dashboard_page.hamburger_menu.click()
    dashboard_page.deliveries_page_select.click()
    deliveries_page.manage_my_box_button.click()

    assert deliveries_page.box_breakdown_component.is_displayed()


@when("Select change delivery dates - quick links")
def _(context):
    dashboard_page = DashboardPage(context)
    time.sleep(10)
    context.browser.execute_script("window.scrollBy(0,1500);")
    time.sleep(10)
    dashboard_page.change_delivery_quick.click()


@when("Select to move the new delivery date")
def _(context):
    dashboard_page = DashboardPage(context)
    time.sleep(5)
    context.browser.execute_script("window.scrollBy(0,200);")
    dashboard_page.date_dropdown.click()

    time.sleep(6)
    context.new_max_delivery_date = \
        DeliveriesPage(context).latest_delivery_day_month_from_change_deliveries_move(
            dashboard_page.new_delivery_date_option.text)
    print(context.new_max_delivery_date, file=sys.stderr)
    dashboard_page.new_delivery_date_option.click()
    # Sleep timer to prevent flakiness when dropdown is closed
    # and user attempts to submit delivery date change
    time.sleep(6)
    context.browser.execute_script("window.scrollBy(0,200);")
    dashboard_page.change_delivery_date_button.click()


@when("Change delivery date from manage my box page")
def _(context):
    deliveries_page = DeliveriesPage(context)
    deliveries_page.change_delivery_date_link.click()
    assert deliveries_page.change_delivery_header

    deliveries_page.new_delivery_date_option.click()

    context.new_max_delivery_date = DeliveriesPage(context).latest_delivery_day_month(deliveries_page.
                                                                                      new_delivery_date_option.text)
    print(context.new_max_delivery_date, file=sys.stderr)

    deliveries_page.submit_change_date.click()
    # Change Delivery Date reason functionality has been removed; so this step is commented out unless it gets re-added
    # assert deliveries_page.change_delivery_date_reason
    # deliveries_page.submit_reason.click()


@then("New estimated delivery date for next delivery is displayed on the deliveries list page")
def _(context):
    deliveries_page = DeliveriesPage(context)
    new_delivery_date = context.new_max_delivery_date
    assert deliveries_page.change_date_confirmation
    assert deliveries_page.check_new_delivery_date(
        new_delivery_date)


@then("The manage box page is showing new delivery date on delivery card section")
def _(context):
    deliveries_page = DeliveriesPage(context)
    new_max_delivery_date = context.new_max_delivery_date

    # We have inconsistent date formats across the tails site.
    # The below code makes sure dates like 11 sept are shown as 11 sep for correct assertions
    new_max_delivery_date_date = new_max_delivery_date.split()[0]
    new_max_delivery_date_month = (new_max_delivery_date.split()[1])[0:3]
    new_max_delivery_date = new_max_delivery_date_date + " " + new_max_delivery_date_month

    assert deliveries_page.convert_date_to_delivery_due_date_format(new_max_delivery_date,
                                                                    "%d %b") in deliveries_page.delivery_due_date.text


@when('subscription is delayed for "(.*)" month via quick links')
def _(context, num_month):
    dashboard_page = DashboardPage(context)
    time.sleep(10)
    dashboard_page.delay_or_pause.click()
    dashboard_page.pause_deliveries.click()

    delivery_page = DeliveriesPage(context)
    if num_month == "1":
        delivery_page.delay_delivery_one_month.click()
    if num_month == "2":
        delivery_page.delay_delivery_two_month.click()
    delivery_page.confirm_pause_delivery.click()


@then('next delivery date is updated by "(.*)" month')
def _(context, num_month):
    delivery_page = DeliveriesPage(context)

    expected_delivery_date_range = \
        delivery_page.delayed_delivery_month(int(num_month), context.subscription_delivery_date)
    # New delivery date shown on pause delivery confirmation page
    actual_next_delivery_window = delivery_page.delay_confirmation_new_delivery_date.text
    assert delivery_page.check_delivery_date_range(actual_next_delivery_window, expected_delivery_date_range)


@when('subscription is delayed for 2 weeks via quick links')
def _(context):
    dashboard_page = DashboardPage(context)
    dashboard_page.delay_or_pause.click()
    dashboard_page.pause_deliveries.click()

    delivery_page = DeliveriesPage(context)
    delivery_page.delay_delivery_two_weeks.click()
    delivery_page.confirm_pause_delivery.click()


@then('next delivery date is updated by 2 weeks')
def _(context):
    delivery_page = DeliveriesPage(context)

    # Increase range of expected dates due to bank-holiday weekends
    relative_days_range = range(11, 17)
    expected_delivery_date_range = delivery_page.delayed_delivery_two_weeks(context.subscription_delivery_date,
                                                                            relative_days_range)
    # New delivery date shown on pause delivery confirmation page
    actual_next_delivery_window = delivery_page.delay_confirmation_new_delivery_date.text
    time.sleep(5)
    assert delivery_page.check_delivery_date_range(actual_next_delivery_window, expected_delivery_date_range)


@given('Get next delivery date from frontyard for customer with store type "(.*)" store id "(.*)"')
def step_impl(context, seed_profile_type, store_id):
    fy = FrontyardPage(context)
    fy_dateformat = '%d %b %Y'

    fy.goto_fy()
    fy.login_fy()
    context.email = generate_email_customer_seed(seed_profile_type, store_id)
    context.customer_id = EmailPage(context).get_customer_id_from_email(context.email)
    fy.search.send_keys(context.email)
    fy.search_button.click()

    fy_food_subscription_date = fy.subscription_next_delivery_date.text

    # Splitting date format in order to display months with 3 letters only eg: Sep
    next_delivery_date_date = fy_food_subscription_date.split()[0]
    next_delivery_date_month = (fy_food_subscription_date.split()[1])[0:3]
    next_delivery_date_year = (fy_food_subscription_date.split()[2])

    # Need this date format in order for asserts to work properly anywhere on tails web pages
    next_delivery_date = next_delivery_date_date + " " + next_delivery_date_month + " " + next_delivery_date_year

    context.subscription_delivery_date = datetime.datetime.strptime(next_delivery_date, fy_dateformat)
    print(context.subscription_delivery_date, file=sys.stderr)


@given('Access to "(.*)" customer account on Frontyard in store id "(.*)"')
def step_impl(context, seed_profile_type, store_id):
    fy = FrontyardPage(context)
    fy.goto_fy()
    fy.login_fy()
    context.email = generate_email_customer_seed(seed_profile_type, store_id)
    context.customer_id = EmailPage(context).get_customer_id_from_email(context.email)
    fy.visit(EmailPage(context).fy_url + "/customers/" + context.customer_id)


@then('"(.*)" product is displayed in the delivery')
def _(context, _product):
    delivery_page = DeliveriesPage(context)
    delivery_page.view_delivery_button.click()
    time.sleep(5)
    assert _product in delivery_page.delivery_breakdown.text


@then('"(.*)" product is not displayed in the delivery')
def _(context, _product):
    delivery_page = DeliveriesPage(context)
    delivery_page.view_delivery_button.click()
    time.sleep(5)
    assert _product not in delivery_page.delivery_breakdown.text


