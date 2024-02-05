from behave import given, then, use_step_matcher

from features.page_objects.home_page import HomePage
from features.page_objects.email_page import EmailPage
from features.page_objects.navigation_page import NavigationPage
from features.page_objects.frontyard import FrontyardPage
from features.page_objects.dashboard_page import DashboardPage
from features.data_seed.provider_state_seeds import *
import time

use_step_matcher("re")


@given('Logged in to "(.*)" customer account "(.*)" and store "(.*)"')
def _(context, country, seed_profile_type, store_id):
    home_page = HomePage(context)
    email_page = EmailPage(context)

    home_page.goto("/")
    navigation = NavigationPage(context)
    email = EmailPage(context)
    time.sleep(5)

    customer_email = generate_email_customer_seed(seed_profile_type, store_id)
    context.customer_id = email.get_customer_id_from_email(customer_email)
    for cookie in context.browser.cookies_to_set:
        context.browser.add_cookie(cookie)

    time.sleep(7)
    home_page.country_select_login(country)
    email_page.country_for_login(country)
    # the following steps passing through password first then username
    # this is to overcome the android keyboard pop up preventing login
    # button click - do not change seq of steps
    email.email_password()

    email.email_login.send_keys(customer_email)
    time.sleep(1)
    navigation.login_button()


@given('Logged in to tails.com store "(.*)" with existing email')
def _(context, country):
    home_page = HomePage(context)
    home_page.goto("/")
    
    navigation = NavigationPage(context)

    for cookie in context.browser.cookies_to_set:
        context.browser.add_cookie(cookie)

    home_page.country_select_login(country)

    email_page = EmailPage(context)
    email_page.country_for_login(country)
    email_page.email_login.send_keys(context.email)
    email_page.password_dashboard_login.send_keys(1234)
    time.sleep(3)
    navigation.account_login.click()
    # DashboardPage(context).dashboard_feed_survey_dismiss()


@given('Attempted password recovery of "(.*)" customer account "(.*)" and store "(.*)"')
def _(context, country, seed_profile_type, store_id):
    home_page = HomePage(context)
    home_page.goto("/")
    navigation = NavigationPage(context)
    login = EmailPage(context)

    customer_email = generate_email_customer_seed(seed_profile_type, store_id)
    context.customer_id = login.get_customer_id_from_email(customer_email)

    for cookie in context.browser.cookies_to_set:
        context.browser.add_cookie(cookie)

    home_page.goto('/signin')
    navigation.forgot_password.click()
    assert login.forgot_password_header
    login.forgot_password_email.send_keys(customer_email)
    login.forgot_password_submit.click()


@given('A customer from "(.*)" customer account "(.*)" and store "(.*)" exist')
def _(context, country, seed_profile_type, store_id):
    home_page = HomePage(context)
    home_page.goto("/")
    login = EmailPage(context)

    customer_email = generate_email_customer_seed(seed_profile_type, store_id)
    context.customer_id = login.get_customer_id_from_email(customer_email)


@then('confirm password reset email is sent')
def _(context):
    # Steps are defined in @given
    email = EmailPage(context)
    assert email.forgot_password_confirmation
    email.forgot_password_OK.click()

    login = EmailPage(context)
    fy_url = login.fy_url
    email.visit(fy_url)


@then('email exists in frontyard')
def _(context):
    fy = FrontyardPage(context)
    fy.goto_fy()
    time.sleep(3)
    fy.login_fy()
    time.sleep(3)
    login = EmailPage(context)
    fy_url = login.fy_url
    time.sleep(5)
    fy.visit(fy_url + "/customers/" + context.customer_id + "/emails")
    time.sleep(5)
    assert fy.forgotemail


@then('customer account loads on frontyard')
def _(context):
    fy = FrontyardPage(context)
    fy.goto_fy()
    fy.login_fy()
    login = EmailPage(context)
    fy_url = login.fy_url
    fy.visit(fy_url + "/customers/" + context.customer_id)
    time.sleep(3)
    assert fy.overview_title
