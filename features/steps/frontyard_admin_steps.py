import json

from behave import when, then, use_step_matcher
from features.page_objects.frontyard import FrontyardPage

use_step_matcher("re")


@when('Submits request to get DSS data')
def _(context):
    frontyard_page = FrontyardPage(context)
    frontyard_page.subscription_checkbox.click()
    frontyard_page.get_email_data.click()
    context.browser.execute_script("arguments[0].click();", frontyard_page.get_dss_data)


@then('Dry food product title in DSS data is displayed with "(.*)"')
def _(context, title):
    frontyard_page = FrontyardPage(context)
    dss_data = json.loads(frontyard_page.get_dss_data_json())
    assert dss_data[0]["comms_type_identifier"] == "delivery-shipping-soon"
    assert dss_data[0]["merge_vars"]["pets"][0]["products"][0]["title"] \
           == title
