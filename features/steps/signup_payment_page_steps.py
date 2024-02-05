import time

from behave import when, use_step_matcher
from features.page_objects.payment_page import PaymentPage

use_step_matcher("re")


@when("Checkout with stripe payment details")
def step_payment_stripe(context):
    payment = PaymentPage(context)
    payment.checkout_stripe_payment()
    time.sleep(5)
