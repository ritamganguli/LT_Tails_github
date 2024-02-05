from behave import when, use_step_matcher
from features.page_objects.motivation_page import MotivationPage
import time

use_step_matcher("re")


@when("Select gain weight motivation for dog food")
def _(context):
    motivation_page = MotivationPage(context)
    motivation = motivation_page.motivation_form
    motivation_page.gain_weight.click()
    time.sleep(5)
    motivation.submit()
    time.sleep(5)
    motivation_info = motivation_page.motivation_info_form
    motivation_info.submit()
