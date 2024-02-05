import time
from behave import*

from features.page_objects.dashboard_page import DashboardPage
from features.page_objects.wftu_page import WFTUPage
from features.page_objects.manual_wet_food_page import ManualWetFoodPage


@When('Customer Orders Extra Wet Food')
def _(context):
    dashboard_page = DashboardPage(context)
    wftu_page = WFTUPage(context)

    #dashboard_page.view_full_deliveries_button.click()
    time.sleep(5)
    dashboard_page.edit_selection.click()
    time.sleep(1)
    dashboard_page.hamburger_menu.click()
    dashboard_page.dashboard_page_select.click()
    context.browser.execute_script("window.scrollBy(0,500);")
    dashboard_page.order_extra_wet_food.click()
    time.sleep(5)
    wftu_page.wftu_get_started_continue.click()
    time.sleep(5)
    wftu_page.wftu_delivery_submit.click()
    # next_full_order_date = wftu_page.next_full_order_date.text
    wftu_page.leave_as_it_is.click()
    time.sleep(5)
    wftu_page.confirm.click()
    context.browser.execute_script("window.scrollBy(0,300);")
    wftu_page.go_to_my_dashboard.click()


@Then('Validate Wet Food being added in upcoming deliveries')
def _(context):
    dashboard_page = DashboardPage(context)
    manual_wet_food_page = ManualWetFoodPage(context)

    dashboard_page.manage_box_cta.click()
    assert manual_wet_food_page.wet_food_box_tray.text == "31 trays"


@When('Customer navigates to wet food shop')
def _(context):
    dashboard_page = DashboardPage(context)
    context.browser.execute_script("window.scrollBy(0,500);")
    dashboard_page.add_wet_food_link.click()


@When('Customer clicks on update wet food')
def _(context):
    dashboard_page = DashboardPage(context)
    context.browser.execute_script("window.scrollBy(0,300);")
    dashboard_page.update_wet_food.click()














