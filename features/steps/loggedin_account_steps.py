from behave import when, then, use_step_matcher
import time

from selenium.webdriver import Keys, ActionChains

from features.page_objects.dashboard_page import DashboardPage
from features.page_objects.account_page import AccountPage
from features.page_objects.navigation_page import NavigationPage


use_step_matcher("re")


@when('Select Account page and confirm "(.*)" displays')
def _(context, header):
    dashboard_page = DashboardPage(context)
    account_page = AccountPage(context)
    navigation = NavigationPage(context)
    time.sleep(10)
    navigation.home_menu.click()
    time.sleep(7)
    dashboard_page.account_page_select.click()
    time.sleep(10)
    account_header = account_page.account_page_header
    time.sleep(7)

    assert account_header.text in header


@when('Update delivery address "(.*)"')
def _(context, del_address):
    account_page = AccountPage(context)
    nav = NavigationPage(context)

    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   account_page.update_delivery)
    account_page.update_delivery.click()
    time.sleep(5)

    update_recipient_name = account_page.update_recipient_name
    delivery_address = account_page.delivery_address

    assert update_recipient_name.get_attribute("value") == "First Last"
    assert delivery_address.text == "7 Kew Foot Road, TW9 2SS"

    account_page.change_address.click()
    time.sleep(3)
    account_page.search_postcode_old_design.send_keys("SM5 4LE")
    nav.escape_keyboard()
    time.sleep(3)
    account_page.search_postcode_old_design.send_keys(Keys.TAB * 0)

    actions = ActionChains(account_page.browser)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(7)
    account_page.new_address.click()
    account_page.select_address_dropdown_deliver_address(del_address)

    account_page.save_changes_button.click()


@when('Update delivery service to DPD')
def _(context):
    account_page = AccountPage(context)
    time.sleep(3)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   account_page.update_delivery)
    account_page.update_delivery.click()
    account_page.Dpd_delivery_service_option.click()
    account_page.save_changes_button.click()


@when('Update delivery instructions to "(.*)"')
def _(context, delivery_instruction):
    account_page = AccountPage(context)
    time.sleep(3)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   account_page.update_delivery)
    account_page.update_delivery.click()
    account_page.update_special_instructions(delivery_instruction)
    account_page.save_changes_button.click()


@when('Update mobile number to use country code "(.*)" and phone number "(.*)"')
def _(context, country_code, phone_number):
    account_page = AccountPage(context)
    time.sleep(3)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   account_page.update_delivery)
    account_page.update_delivery.click()
    account_page.phone_number.send_keys(phone_number)
    account_page.save_changes_button.click()


@then('Confirm address "(.*)" displays')
def _(context, _address):
    account_page = AccountPage(context)
    time.sleep(3)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   account_page.address_account_page)
    address = account_page.address_account_page
    assert _address in address.text


@then('Confirm delivery service is checked')
def _(context):
    account_page = AccountPage(context)
    time.sleep(3)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   account_page.update_delivery)
    account_page.update_delivery.click()
    time.sleep(3)
    account_page.dpd_check()


@then('Confirm delivery instruction is "(.*)"')
def _(context, delivery_instruction):
    account_page = AccountPage(context)
    time.sleep(3)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   account_page.special_instructions_account_page)
    assert delivery_instruction == account_page.special_instructions_account_page.text


@then('Confirm updated mobile number is "(.*)"')
def _(context, mobile_number):
    account_page = AccountPage(context)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   account_page.address_account_page)
    assert mobile_number in account_page.address_account_page.text


@when("Select update password")
def _(context):
    account_page = AccountPage(context)

    account_page.change_password_button.click()
    time.sleep(5)


@when("Add current and new password")
def _(context):
    account_page = AccountPage(context)

    account_page.current_password.send_keys("1234")
    time.sleep(5)
    account_page.new_password.send_keys("123456")
    time.sleep(5)
    account_page.confirm_new_password.send_keys("123456")
    time.sleep(5)

    account_page.save_password_button.click()
    time.sleep(5)


@then('Confirm account page "(.*)" displays')
def _(context, _notification):
    account_page = AccountPage(context)

    notification = account_page.account_page_notification

    assert notification.text == _notification


@when("Select update your details")
def _(context):
    account_page = AccountPage(context)

    account_page.update_details.click()
    time.sleep(5)


@when("Cancel my deliveries")
def _(context):
    account_page = AccountPage(context)
    time.sleep(3)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   account_page.cancel_link)
    account_page.cancel_link.click()
    time.sleep(3)
    account_page.cancel_cta.click()
    time.sleep(3)


@when('Select the food as reason for cancelling and confirm')
def _(context):
    account_page = AccountPage(context)
    time.sleep(6)
    context.browser.execute_script("window.scrollBy(0,300);")
    account_page.food_reason_cancel.click()
    time.sleep(6)
    context.browser.execute_script("window.scrollBy(0,600);")
    account_page.confirm_cancel.click()
    time.sleep(3)


@then('Account cancelled and "(.*)" displays')
def _(context, header):
    account_page = AccountPage(context)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   account_page.deliveries_cancelled)
    cancelled = account_page.deliveries_cancelled

    assert cancelled.text == header
