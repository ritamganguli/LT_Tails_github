import time
from behave import*

from features.page_objects.update_portion_page import UpdatePortionPage


@When('Updates Wet Food Portion')
def _(context):
    update_portion_page = UpdatePortionPage(context)
    time.sleep(20)
    update_portion_page.enter_amount.click()
    update_portion_page.input_grams_link.click()
    update_portion_page.enter_grams.clear()
    update_portion_page.enter_grams.send_keys(300)
    update_portion_page.next_button.click()
    time.sleep(7)
    update_portion_page.next_button.click()
    time.sleep(7)
    update_portion_page.next_button.click()
    context.browser.execute_script("window.scrollBy(0,700);")
    time.sleep(10)
    context.browser.execute_script("window.scrollBy(0,200);")
    update_portion_page.next_button.click()
    time.sleep(1)
