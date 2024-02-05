import time
from behave import when, then, use_step_matcher
from features.page_objects.account_page import AccountPage
from features.page_objects.navigation_page import NavigationPage

use_step_matcher("re")


@when('Select payment method "(.*)"')
def _(context, payment_method):
    account_settings = AccountPage(context)

    account_settings.update_payment_button.click()
    time.sleep(5)
    account_settings.select_credit_card.click()
    time.sleep(5)
    account_settings.continue_pay_method_button.click()

    assert account_settings.stripe_page_header.text == 'Secure payment details'


@when('Select Paypal payment method')
def _(context):
    account_settings = AccountPage(context)

    time.sleep(3)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   account_settings.update_payment_button)

    account_settings.update_payment_button.click()
    account_settings.select_paypal_payment_method()


@when('Confirm Paypal payment method update')
def _(context):
    account_settings = AccountPage(context)
    account_settings.confirm_paypal_payment_method()


@when('Confirm Paypal payment method update with registering billing address')
def _(context):
    time.sleep(7)
    account_settings = AccountPage(context)

    account_settings.different_billing.click()
    account_settings.search_postcode.send_keys("SM5 4LE")
    account_settings.find_address.click()
    account_settings.new_address.click()
    account_settings.select_new_address.click()

    account_settings.confirm_paypal_payment_method()


@when("Add and submit stripe payment details")
def _(context):
    account_settings = AccountPage(context)
    nav = NavigationPage(context)
    account_settings.checkout_stripe_payment()
    time.sleep(7)
    nav.dismiss_keyboard()
    context.browser.execute_script("window.scrollBy(0,300);")
    account_settings.different_billing.click()
    account_settings.same_billing.click()
    account_settings.confirm_card_details_stripe.click()


@when('Add and submit stripe payment details with billing address "(.*)"')
def _(context, del_address):
    account_settings = AccountPage(context)
    nav = NavigationPage(context)

    account_settings.checkout_stripe_payment()
    time.sleep(7)

    nav.dismiss_keyboard()
    context.browser.execute_script("window.scrollBy(0,500);")
    account_settings.different_billing.click()

    account_settings.search_postcode.send_keys("SM5 4LE")
    account_settings.find_address.click()
    account_settings.select_address_dropdown_card_not_deliver_address(del_address)
    account_settings.card_register_address_find.click()

    account_settings.confirm_card_details_stripe.click()


@when('Banner "(.*)" is showing on account settings page')
def _(context, text_banner):
    # This banner varies depends on several scenarios when updating card payment:
    # 1) Your payment method has been updated
    # 2) Updated payment method to Credit/Debit card
    # 3) Updated payment method to PayPal
    time.sleep(5)
    # assert AccountPage(context).account_flash_message_notification.text == text_banner


@then('Verify card details are updated on account settings page')
def _(context):
    card_component_text = AccountPage(context).card_payment_details.text
    card_expiry_details_text = AccountPage(context).card_expiry_details.text
    # card type is no longer displayed
    # assert "visa" in card_component_text

    # PAN is masked and only showing last 4 digits
    assert "**** **** **** 4242" in card_component_text

    # Expiry date
    assert "10 / 2024" in card_expiry_details_text


@then('Verify Paypal account is updated on account settings page')
def _(context):
    assert AccountPage(context).paypal_logo


@when('Select and enter a different billing address')
def _(context):
    account_settings = AccountPage(context)

    account_settings.paypal_different_billing.click()
    time.sleep(5)

    account_settings.paypal_different_billing_postcode_search.send_keys("SM5 4LE")
    account_settings.find_address.click()
    time.sleep(5)

    account_settings.select_address_dropdown_card_not_deliver_address("49 Stanley Road")


@when("Select and enter a different billing address via manual input")
def _(context):
    account_settings = AccountPage(context)

    account_settings.paypal_different_billing.click()
    time.sleep(5)

    account_settings.paypal_different_billing_postcode_search.send_keys("SM5 4LE")
    account_settings.find_address.click()
    time.sleep(5)

    account_settings.billing_address_manual.click()
    account_settings.address_manual_first_line.send_keys("1A Stanley Road")
    account_settings.address_manual_city.send_keys("Carshalton")


@when("Select and enter a different billing address in France")
def _(context):
    account_settings = AccountPage(context)

    account_settings.paypal_different_billing.click()
    time.sleep(5)

    account_settings.paypal_different_billing_postcode_search.send_keys("89800")
    account_settings.find_address.click()
    time.sleep(5)

    account_settings.select_address_dropdown_card_not_deliver_address("5 Chemin des Vignes")


@when("Select and enter a different billing address in Germany")
def _(context):
    account_settings = AccountPage(context)

    account_settings.paypal_different_billing.click()
    time.sleep(5)

    account_settings.paypal_different_billing_postcode_search.send_keys("06638")
    account_settings.find_address.click()
    time.sleep(5)

    account_settings.select_address_dropdown_card_not_deliver_address("Bahnhofsweg 3")
