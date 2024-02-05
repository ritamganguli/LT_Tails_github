from behave import when
import time

from selenium.webdriver.common import actions

from features.page_objects.dashboard_page import DashboardPage
from features.page_objects.manual_wet_food_page import ManualWetFoodPage


@when('Adds trays to wet food selection')
def _(context):
    dashboard_page = DashboardPage(context)
    manual_wet_food_page = ManualWetFoodPage(context)
    time.sleep(10)
    manual_wet_food_page.check_product_available()
    context.browser.execute_script("window.scrollBy(0,900);")
    manual_wet_food_page.increase_trays_product_871.click()
    time.sleep(5)

    manual_wet_food_page.add_more_trays.click()
    time.sleep(7)

    manual_wet_food_page.decrease_trays_product_871.click()
    manual_wet_food_page.recipe_1.clear()
    manual_wet_food_page.recipe_1.send_keys(31)

    time.sleep(5)
    manual_wet_food_page.add_wf_button.click()
    time.sleep(5)
    manual_wet_food_page.add_next_delivery.click()
    time.sleep(5)
    dashboard_page.hamburger_menu.click()
    time.sleep(5)
    dashboard_page.dashboard_page_select.click()



