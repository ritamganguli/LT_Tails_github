from behave import when, then, use_step_matcher
import time

from features.page_objects.dashboard_page import DashboardPage
from features.page_objects.home_page import HomePage
from features.page_objects.email_page import EmailPage
from features.page_objects.navigation_page import NavigationPage
from features.page_objects.account_page import AccountPage
from features.data_seed.provider_state_seeds import *

use_step_matcher("re")


@then('customer lands on dashboard')
def _(context):
    assert DashboardPage(context).header_pet_name.text == 'Qa Champ'


@then('Signup completed and "(.*)" display')
def _(context, my_dashboard):
    signup_complete = DashboardPage(context)
    dashboard_link = signup_complete.continue_dashboard
    time.sleep(5)
    assert dashboard_link.text == my_dashboard
    signup_complete.continue_dashboard.click()
    time.sleep(5)


@then('Signup completed and dutch "(.*)" display')
def _(context, my_dashboard):
    signup_complete = DashboardPage(context)
    dashboard_link = signup_complete.nl_continue_dashboard
    assert dashboard_link.text == my_dashboard
    signup_complete.nl_continue_dashboard.click()


@then('Signup completed and france "(.*)" display')
def _(context, fr_dashboard):
    signup_complete = DashboardPage(context)
    time.sleep(5)
    dashboard_link = signup_complete.fr_continue_dashboard
    assert dashboard_link.text == fr_dashboard
    signup_complete.fr_continue_dashboard.click()


@then('Signup completed and german "(.*)" display')
def _(context, de_dashboard):
    signup_complete = DashboardPage(context)
    dashboard_link = signup_complete.de_continue_dashboard
    assert dashboard_link.text == de_dashboard
    signup_complete.de_continue_dashboard.click()


@when('Click cancel in the quick links section for "(.*)"')
def _(context, country):
    dashboard_page = DashboardPage(context)
    account_page = AccountPage(context)
    time.sleep(10)

    if country == "France":
        dashboard_page.cancel_quick_link_FR.click()
    if country == "Germany":
        # actions = ActionChains(dashboard_page.browser)
        dashboard_page.cancel_quick_link_DE.click()
    context.browser.execute_script("window.scrollBy(0,600);")
    time.sleep(3)
    account_page.cancel_cta.click()
    time.sleep(3)


@when("Select update and restart their cancelled deliveries")
def _(context):
    dashboard_page = DashboardPage(context)
    time.sleep(3)
    dashboard_page.hamburger_menu.click()
    time.sleep(3)
    dashboard_page.dashboard_page_select.click()
    dashboard_page.wait_for_new_account_loading_animation_to_disappear()
    dashboard_page.restart_cancelled_subscription_button.click()


@when("Select update and resume their paused deliveries")
def _(context):
    dashboard_page = DashboardPage(context)
    time.sleep(7)
    dashboard_page.hamburger_menu.click()
    dashboard_page.dashboard_page_select.click()
    dashboard_page.wait_for_new_account_loading_animation_to_disappear()
    dashboard_page.resume_paused_subscription_button.click()


@when("Restart my deliveries by confirming the profile and delivery date")
def _(context):
    dashboard_page = DashboardPage(context)
    dashboard_page.next_button_reactivate.click()
    dashboard_page.restart_confirm.click()


@then('Confirm "(.*)" displays on the restart delivery confirmation page')
def _(context, confirmation_message):
    dashboard_page = DashboardPage(context)

    assert confirmation_message in dashboard_page.delivery_header_cancelled.text


@when("Select delay or pause on the dashboard and indefinite pause")
def _(context):
    dashboard_page = DashboardPage(context)
    dashboard_page.delay_or_pause.click()
    dashboard_page.pause_deliveries.click()
    dashboard_page.pause_indefinitely.click()
    dashboard_page.confirm_button.click()


@when("Select price as the reason for pausing")
def _(context):
    dashboard_page = DashboardPage(context)
    dashboard_page.pause_reason_price_tile.click()
    dashboard_page.pause_deliveries_button.click()


@when("Add a new dog using quick link")
def _(context):
    dashboard_page = DashboardPage(context)
    dashboard_page.add_dog_quick_link.click()
    time.sleep(3)


@when("Select log out")
def _(context):
    dashboard_page = DashboardPage(context)
    time.sleep(2)
    dashboard_page.hamburger_menu.click()
    dashboard_page.log_out.click()
    time.sleep(5)


@then('Confirm logout message "(.*)" displays')
def _(context, log_out):
    dashboard_page = DashboardPage(context)
    notification = dashboard_page.logged_out

    assert notification.text == log_out


@when('Log in to "(.*)" customer account "(.*)" and store "(.*)"')
def _(context, country, seed_profile_type, store_id):
    home_page = HomePage(context)
    email_page = EmailPage(context)

    home_page.goto("/")
    navigation = NavigationPage(context)
    email = EmailPage(context)

    customer_email = generate_email_customer_seed(seed_profile_type, store_id)

    for cookie in context.browser.cookies_to_set:
        context.browser.add_cookie(cookie)

    # home_page.select_country()
    time.sleep(5)
    home_page.country_select_login(country)
    email_page.country_for_login(country)
    # the following steps passing through password first then username
    # this is to overcome the android keyboard pop up preventing login
    # button click - do not change seq of steps
    email.email_password()
    email.email_login.send_keys(customer_email)
    navigation.login_button()


@then('Confirm "(.*)" displayed on the dashboard')
def _(context, qa_champ):
    dashboard_page = DashboardPage(context)
    dog_name = dashboard_page.dashboard_header

    assert dog_name.text == qa_champ


@then('Confirm "(.*)" displayed confirming remained on the dashboard')
def _(context, links):
    dashboard_page = DashboardPage(context)
    header = dashboard_page.quick_links_header

    assert links == header.text


@when('Signup completed for "(.*) and "(.*)" display')
def _(context, country, my_dashboard):
    dashboard = DashboardPage(context)
    dashboard_link = dashboard.continue_dashboard
    assert dashboard_link.text == my_dashboard
    dashboard.continue_dashboard.click()
    time.sleep(5)


@when('Navigates to manage my box page from Dashboard')
def _(context):
    dashboard_page = DashboardPage(context)
    time.sleep(20)
    context.browser.execute_script("window.scrollBy(0,400);")
    dashboard_page.manage_box_cta.click()

