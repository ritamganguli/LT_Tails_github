from behave import when, use_step_matcher
import time

from features.page_objects.ideal_test_page import IdealTestPage

use_step_matcher("re")


@when('Checkout with "(.*)" ideal payment details')
def step_payment_stripe(context, status):
    ideal = IdealTestPage(context)

    time.sleep(10)
    ideal.yes_button.click()
    ideal.scroll_down_page()
    time.sleep(10)

    ideal.continue_button.click()

    ing_button = ideal.ing_button
    ing_button.click()
    time.sleep(4)

    payment_status_button = ideal.mollie_status_button(status)
    assert payment_status_button.text == status
    payment_status_button.click()
    ideal.scroll_down_page()
    continue_button_mollie = ideal.continue_button_mollie
    time.sleep(5)
    continue_button_mollie.click()
