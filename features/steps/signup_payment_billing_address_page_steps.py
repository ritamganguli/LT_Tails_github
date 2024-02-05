from behave import when, use_step_matcher
from features.page_objects.payment_billing_address_page import BillingAddressPage
import time

use_step_matcher("re")


@when('Checkout with stripe billing address with post code lookup "(.*)"')
def checkout_with_stripe_billing_address_postcode_lookup(context, country):
    # Country list:  UK, NI, DE, FR, etc..
    billing_address = BillingAddressPage(context)
    billing_address.input_test_card_payment_details()
    billing_address.add_billing_address_with_postcode_lookup(country)
    billing_address.checkout_button.click()


@when('Checkout with paypal billing address with post code lookup "(.*)"')
def checkout_with_paypal_billing_address_postcode_lookup(context, country):
    billing_address = BillingAddressPage(context)
    time.sleep(1)

    billing_address.checkout_button.click()


@when('Checkout with stripe billing address with manual address input "(.*)"')
def checkout_with_stripe_billing_address_manual_address(context, country):
    billing_address = BillingAddressPage(context)
    billing_address.input_test_card_payment_details()
    billing_address.add_billing_address_with_manual_address_input(country)
    billing_address.checkout_button.click()


@when('Checkout with paypal billing address with manual address input "(.*)"')
def checkout_with_paypal_billing_address_manual_address(context, country):
    billing_address = BillingAddressPage(context)
    time.sleep(2)
    billing_address.add_billing_address_with_manual_address_input(country)
    time.sleep(2)
    if country == "FR":
        billing_address.scroll_down_page()
    time.sleep(2)
    billing_address.checkout_button.click()


@when('Confirm checkout with paypal')
def _(context):
    time.sleep(5)
    billing_address = BillingAddressPage(context)
    billing_address.scroll_down_page()
    time.sleep(2)
    billing_address.checkout_button.click()
