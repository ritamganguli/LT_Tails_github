from behave import when, then, use_step_matcher
import time
from features.page_objects.navigation_page import NavigationPage
from features.page_objects.email_page import EmailPage
from features.page_objects.project_box_pages import ProjectBoxPages
from features.page_objects.frontyard import FrontyardPage

use_step_matcher("re")


@then('complete signup with email "(.*)"')
def _(context, lang):
    email = EmailPage(context)
    email_form = email.email_form

    email.create_random_email()
    saved_email = email.select_by_input_value("#email")

    email.opt_in_no.click()
    email.opt_in_yes.click()
    email.opt_in_no.click()
    email.scroll_to_bottom_of_page()
    email_form.submit()

    box_page = ProjectBoxPages(context)

    time.sleep(2)
    box_page.add_to_box_button.click()
    time.sleep(5)
    treats_page = ProjectBoxPages(context)
    treats_page.go_to_box_button.click()

    time.sleep(10)
    navigation = NavigationPage(context)
    navigation.home_logo.click()
    time.sleep(7)
    navigation.home_menu.click()
    navigation.scroll_to_bottom_of_page()
    time.sleep(2)
    if lang == "France":
        navigation.fr_menu_log_out.click()
    if lang == "English":
        navigation.menu_log_out.click()
    if lang == "Germany":
        navigation.de_menu_log_out.click()
    if lang == "Austria":
        navigation.de_menu_log_out.click()
    if lang == "Dutch":
        navigation.nl_menu_log_out.click()
    time.sleep(2)
    navigation.home_logo.click()
    time.sleep(5)
    navigation.home_menu.click()
    time.sleep(5)
    navigation.scroll_to_bottom_of_page()
    time.sleep(10)
    navigation.menu_log_in.click()
    time.sleep(5)
    email.email_login.send_keys(saved_email)
    time.sleep(7)
    navigation.account_login.click()


@when("Complete email page")
def _(context):
    email = EmailPage(context)

    time.sleep(10)

    email_form = email.email_form
    context.browser.execute_script("window.scrollBy(0,200);")
    email.create_random_email()
    time.sleep(7)
    email.opt_in_no.click()
    email.opt_in_yes.click()
    email.opt_in_no.click()
    email.scroll_to_bottom_of_page()
    time.sleep(20)
    email_form.submit()
    time.sleep(7)


@when("Complete email page for prod")
def _(context):
    email = EmailPage(context)
    time.sleep(50)
    email_form = email.email_form

    email.create_random_email_prod()
    email.opt_in_no.click()
    email.scroll_to_bottom_of_page()
    email_form.submit()
    time.sleep(25)


@then("On email selecting Yes for communication Frontyard shows the customer as contactable")
def _(context):
    email = EmailPage(context)
    time.sleep(10)
    email_form = email.email_form

    email.create_random_email()
    saved_email = email.select_by_input_value("#email")
    email.opt_in_yes.click()
    email.scroll_to_bottom_of_page()
    email_form.submit()

    fy_url = email.fy_url
    email.visit(fy_url)

    fy = FrontyardPage(context)
    fy.goto_fy()
    fy.login_fy()
    fy.search.send_keys(saved_email)
    fy.search_button.click()
    time.sleep(15)
    assert fy.contactable


@then("On email selecting No for communication Frontyard shows the customer as not contactable")
def _(context):
    email = EmailPage(context)

    time.sleep(10)
    email_form = email.email_form

    email.create_random_email()
    saved_email = email.select_by_input_value("#email")
    email.opt_in_no.click()
    email.scroll_to_bottom_of_page()
    email_form.submit()

    fy_url = email.fy_url
    email.visit(fy_url)

    fy = FrontyardPage(context)
    fy.goto_fy()
    fy.login_fy()
    fy.search.send_keys(saved_email)
    fy.search_button.click()
    time.sleep(10)
    assert fy.donotcontact


@when('Complete email page for petname "(.*)"')
def _(context, petname):
    email = EmailPage(context)
    email_form = email.email_form

    email.create_random_email_suitability(petname)
    # saved_email = email.select_by_input_value("#email")
    time.sleep(7)
    email.opt_in_no.click()
    email.opt_in_yes.click()
    email.opt_in_no.click()
    email.scroll_to_bottom_of_page()
    email_form.submit()


@then('email step is in a disabled state')
def _(context):
    email = EmailPage(context)
    box_page = ProjectBoxPages(context)
    email_form = email.email_form
    email_input = email.email_input

    assert email_input.is_enabled()
    assert "send you free samples" not in email_form.text

    email.email_submit.click()
    assert "Please complete email" in email.email_error.text

    email.create_random_email()
    assert email.marketing_preference_form.is_enabled()
    opt_in_no = email.opt_in_no
    opt_in_no.is_selected()
    email.opt_in_yes.click()
    opt_in_no.click()
    email.scroll_to_bottom_of_page()
    time.sleep(2)
    email_form.submit()
    time.sleep(20)
    assert "unique feeding plan" in box_page.core_diet_header.text
