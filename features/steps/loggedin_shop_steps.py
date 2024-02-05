from behave import when, then, use_step_matcher
import time
from features.page_objects.dashboard_page import DashboardPage
from features.page_objects.feeding_plan_loggedin_page import FeedingPage
from features.page_objects.shop_page import ShopPage

use_step_matcher("re")


@when('Select Shop page and confirm "(.*)" displays')
def _(context, product_):
    dashboard_page = DashboardPage(context)
    shop_page = ShopPage(context)
    time.sleep(10)

    dashboard_page.hamburger_menu.click()
    time.sleep(5)

    dashboard_page.shop_page_select.click()
    time.sleep(10)

    shop_page.products_receiving.click()
    prod = shop_page.product(product_)
    # contains = text
    assert prod.text == product_
    time.sleep(5)


@when('Navigates to shop page & clicks on Wet food')
def _(context):
    dashboard_page = DashboardPage(context)
    shop_page = ShopPage(context)
    time.sleep(7)

    dashboard_page.hamburger_menu.click()
    time.sleep(5)

    dashboard_page.shop_page_select.click()
    time.sleep(10)
    context.browser.execute_script("window.scrollBy(0,200);")
    shop_page.products_receiving.click()
    context.browser.execute_script("window.scrollBy(0,400);")
    shop_page.wet_food_image.click()
    time.sleep(10)


@when('Select chicken biscuits in "(.*)" and add into deliveries')
def _(context, country_for):
    shop_page = ShopPage(context)

    time.sleep(2)
    shop_page.add_chicken_biscuits.click()
    time.sleep(10)

    chicken_biscuits = shop_page.biscuits_header
    if country_for == "France":
        assert chicken_biscuits.text == "Biscuits au poulet"
    if country_for == "United Kingdom":
        assert chicken_biscuits.text == "Chicken Biscuits"
    if country_for == "Deutschland":
        assert chicken_biscuits.text == "Hühnchen-Kekse"
    time.sleep(3)

    shop_page.add_delivery.click()


@when("Remove chicken biscuits from deliveries")
def _(context):
    shop_page = ShopPage(context)
    shop_page.edit_chicken_biscuits.click()
    shop_page.pause_chicken_biscuits.click()
    time.sleep(3)


@then('Confirm "(.*)" displayed on shop page in the saved selection')
def _(context, next_delivery):
    shop_page = ShopPage(context)

    chicken_order = shop_page.saved_quantity
    assert next_delivery in chicken_order.text


@when('Select add wet food in "(.*)"')
def _(context, country_for):
    shop_page = ShopPage(context)
    time.sleep(7)
    shop_page.wet_food_add_button.click()
    time.sleep(3)

    header = shop_page.wet_food_header

    if country_for == "France":
        assert "Les barquettes" in header.text
    if country_for == "United Kingdom":
        assert "wet food" in header.text
    if country_for == "Deutschland":
        assert "Nassfutter" in header.text


@when("Enter the amount to feed per day")
def _(context):
    shop_page = ShopPage(context)
    feeding_plan_loggedin_page = FeedingPage(context)

    shop_page.add_amount.click()
    feeding_plan_loggedin_page.add_wet_food.click()
    time.sleep(3)
    feeding_plan_loggedin_page.next_button.click()
    time.sleep(3)
    feeding_plan_loggedin_page.next_button.click()
    time.sleep(3)
    feeding_plan_loggedin_page.next_button.click()
    time.sleep(18)
    feeding_plan_loggedin_page.next_button.click()
    time.sleep(10)


@when("Add different flavours of wet food and confirm the selection")
def _(context):
    shop_page = ShopPage(context)
    shop_page.select_wet_flavours.click()
    time.sleep(3)
    shop_page.surprise_flavours.click()
    time.sleep(5)
    shop_page.confirm_wet_trays.click()
    time.sleep(5)
    shop_page.add_to_delivery.click()
    time.sleep(15)


@then('Confirm "(.*)" displays on the order summary')
def _(context, product):
    shop_page = ShopPage(context)
    time.sleep(15)
    shop_page.order_details.click()
    time.sleep(5)
    assert shop_page.chicken_biscuits_delivery.text == product


@then("Confirm 150g tray premium wet food available")
def _(context):
    signup_complete = DashboardPage(context)
    signup_complete.continue_dashboard.click()
    time.sleep(5)
    dashboard_page = DashboardPage(context)
    shop_page = ShopPage(context)
    time.sleep(7)
    dashboard_page.hamburger_menu.click()
    shop_page.dismiss_survey()
    time.sleep(10)
    dashboard_page.shop_page_select.click()
    time.sleep(5)
    shop_page.dismiss_survey()
    shop_page.wet_food_add_button.click()
    time.sleep(5)
    shop_page.switch_150gr_tray.click()
    time.sleep(10)

    shop_page = ShopPage(context)
    assert shop_page.simply_delicious_beef_with_parsley.text == "Simply Delicious Beef with Parsley"
    assert shop_page.simply_irresistible_chicken_with_rosemary.text == "Simply Irresistible Chicken with Rosemary"
    assert shop_page.succulent_poultry_pie_with_green_beans.text == "Succulent Poultry Pie with Green Beans"


@then("Confirm 150g tray premium wet food available from excluded")
def _(context):
    signup_complete = DashboardPage(context)
    signup_complete.continue_dashboard.click()
    time.sleep(5)
    dashboard_page = DashboardPage(context)
    shop_page = ShopPage(context)
    time.sleep(7)
    dashboard_page.hamburger_menu.click()
    shop_page.dismiss_survey()
    time.sleep(10)
    dashboard_page.shop_page_select.click()
    time.sleep(5)
    shop_page.dismiss_survey()
    shop_page.wet_food_add_button.click()
    time.sleep(10)
    shop_page.switch_150gr_tray.click()
    time.sleep(10)
    shop_page.view_excluded_wet_food.click()
    assert shop_page.succulent_poultry_pie_with_green_beans.text == "Succulent Poultry Pie with Green Beans"
    assert shop_page.simply_irresistible_chicken_with_rosemary.text == "Simply Irresistible Chicken with Rosemary"


@then('Confirm 150g tray premium wet food available from excluded with "(.*)" warning')
def _(context, puppy_wheat):
    signup_complete = DashboardPage(context)
    signup_complete.continue_dashboard.click()
    time.sleep(5)
    dashboard_page = DashboardPage(context)
    shop_page = ShopPage(context)
    time.sleep(7)
    dashboard_page.hamburger_menu.click()
    shop_page.dismiss_survey()
    time.sleep(10)
    dashboard_page.shop_page_select.click()
    time.sleep(5)
    shop_page.dismiss_survey()
    shop_page.wet_food_add_button.click()
    time.sleep(10)
    shop_page.switch_150gr_tray.click()
    shop_page.switch_300gr_tray.click()
    shop_page.switch_150gr_tray.click()
    time.sleep(15)
    excluded = shop_page.view_excluded_wet_puppy_wheat
    assert puppy_wheat in excluded.text


@then('Confirm 150g tray premium wet food available from excluded with "(.*)" hypo warning')
def _(context, dalmation_hypo):
    signup_complete = DashboardPage(context)
    signup_complete.continue_dashboard.click()
    time.sleep(5)
    dashboard_page = DashboardPage(context)
    shop_page = ShopPage(context)
    time.sleep(7)
    dashboard_page.hamburger_menu.click()
    shop_page.dismiss_survey()
    time.sleep(10)
    dashboard_page.shop_page_select.click()
    time.sleep(5)
    shop_page.dismiss_survey()
    shop_page.wet_food_add_button.click()
    time.sleep(10)
    shop_page.switch_150gr_tray.click()
    shop_page.switch_300gr_tray.click()
    shop_page.switch_150gr_tray.click()
    time.sleep(15)
    excluded = shop_page.view_excluded_wet_hypo
    assert dalmation_hypo in excluded.text


@then("Confirm 150g tray premium available in shop if user opt in wet food already")
def _(context):
    signup_complete = DashboardPage(context)
    signup_complete.continue_dashboard.click()
    time.sleep(5)
    dashboard_page = DashboardPage(context)
    shop_page = ShopPage(context)
    time.sleep(5)
    dashboard_page.hamburger_menu.click()
    time.sleep(7)
    dashboard_page.shop_page_select.click()
    shop_page.wet_food_add_button.click()
    time.sleep(5)
    shop_page.wet_food_edit_button.click()
    time.sleep(5)
    shop_page.choose_my_tray.click()
    time.sleep(7)
    assert shop_page.simply_irresistible_chicken_with_rosemary.text == "Simply Irresistible Chicken with Rosemary"
    assert shop_page.succulent_poultry_pie_with_green_beans.text == "Succulent Poultry Pie with Green Beans"


@when('Navigates to Shop page')
def _(context):
    dashboard_page = DashboardPage(context)
    time.sleep(10)

    dashboard_page.hamburger_menu.click()
    time.sleep(5)

    dashboard_page.shop_page_select.click()
    time.sleep(15)


@when('Customer clicks on the Wet Food Panel')
def _(context):
    shop_page = ShopPage(context)
    time.sleep(10)

    shop_page.wet_food_add_button.click()
    time.sleep(5)


@then('Customer should be directed to Manual Shop')
def _(context):
    shop_page = ShopPage(context)
    time.sleep(5)

    current_url = shop_page.get_current_url()

    expected_text = "wet-food-selection"

    assert expected_text in current_url


@then('Customer should be directed to Auto Shop')
def _(context):
    shop_page = ShopPage(context)
    time.sleep(5)

    current_url = shop_page.get_current_url()

    expected_text = "wet-food/mix-selection"

    assert expected_text in current_url


@when('Adds "(.*)" product')
def _(context, _product):
    shop = ShopPage(context)
    time.sleep(5)

    if _product.lower() == "natural chews":
        shop.natural_chews_add_gb.click()
    if _product.lower() == "octopus toy":
        shop.octopus_add.click()
    if _product.lower() == "poo bags":
        shop.poo_bags_add.click()
    if _product.lower() == "hand baked chicken biscuits":
        shop.chicken_biscuits_add.click()
    if _product.lower() == "hand baked duck biscuits":
        shop.duck_biscuits_add.click()
    if _product.lower() == "cold pressed duck bites":
        shop.cold_press_duck_add.click()

    shop.add_subscription.click()


@when("Navigates to manage my box page from shop")
def _(context):
    shop = ShopPage(context)
    time.sleep(5)
    shop.deliveries_icon.click()
    time.sleep(15)


@then('"(.*)" product is not displayed in the shop')
def _(context, _product):
    shop = ShopPage(context)
    assert _product not in shop.shop_content.text


@when('Navigates to PDP for "(.*)" product')
def _(context, _product):
    shop = ShopPage(context)
    shop.go_to_product_pdp_by_name(_product)
    time.sleep(5)
    assert _product in shop.pdp_title.text


@when('Customer removes product')
def _(context):
    shop = ShopPage(context)
    shop.counter_minus.click()


@when("Adds product on the PDP")
def _(context):
    shop = ShopPage(context)
    shop.scroll_down_page()
    shop.add_subscription.click()


@when('Navigates to PDP for "(.*)" product when in subscription')
def _(context, _product):
    shop = ShopPage(context)
    shop.products_receiving_dropdown.click()
    shop.go_to_product_pdp_by_name(_product)
    time.sleep(5)
    assert _product in shop.pdp_title.text
    time.sleep(3)