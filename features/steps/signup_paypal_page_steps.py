from behave import when, use_step_matcher
import time
from features.page_objects.paypal_page import PaypalPage


use_step_matcher("re")


@when('Input Paypal credentials for "(.*)" store')
def _(context, country):
    time.sleep(10)
    # the next step will fail if running headless due to not being able to resize PayPal's window.
    PaypalPage(context).login_to_paypal(country)
    time.sleep(3)
