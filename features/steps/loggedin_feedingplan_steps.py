import sys
from behave import when, then, use_step_matcher
import time

from features.page_objects.dashboard_page import DashboardPage
from features.page_objects.feeding_plan_loggedin_page import FeedingPage

use_step_matcher("re")


@when("Navigates to feeding plan page")
def _(context):
    feeding_plan_page = FeedingPage(context)
    dashboard_page = DashboardPage(context)
    time.sleep(15)
    dashboard_page.hamburger_menu.click()
    # navigation.home_menu.click()
    dashboard_page.feeding_plan_page_select.click()
    time.sleep(5)
    assert feeding_plan_page.feeding_plan_page_header.is_displayed()


@when("Navigates to wet food portions flow via the feeding plan page")
def _(context):
    feeding_plan_page = FeedingPage(context)

    feeding_plan_page.update_portions_link.click()

    assert feeding_plan_page.wet_portion_form.is_displayed()


@when('Modifies wet food tray size to "(.*)" tray')
def _(context, chosen_tray_option):
    feeding_plan_page = FeedingPage(context)

    print("number of options ", len(feeding_plan_page.get_select_element(feeding_plan_page.amount_locator_id).options),
          file=sys.stderr)
    time.sleep(2)
    for option in feeding_plan_page.get_select_element(feeding_plan_page.amount_locator_id).options:
        print("current option " + option.get_attribute('value'), file=sys.stderr)
        if option.get_attribute('value') == chosen_tray_option:
            assert option.get_attribute('value') == chosen_tray_option
            feeding_plan_page.next_button.click()
            assert feeding_plan_page.treats_choice.is_displayed()
            break
        else:
            feeding_plan_page.click_element_js(feeding_plan_page.increase_tray_size_icon)
            time.sleep(0.5)


@when('Selects rough estimation "(.*)" for treats and other food')
def _(context, portion):
    feeding_plan_page = FeedingPage(context)

    feeding_plan_page.get_treat_option_element(portion).click()
    feeding_plan_page.next_button.click()
    assert feeding_plan_page.dry_recommended.is_displayed()


@when('Selects default option to update dry food as recommended option')
def _(context):
    feeding_plan_page = FeedingPage(context)
    feeding_plan_page.next_button.click()
    assert feeding_plan_page.price_header.is_displayed()


@when('Confirm new daily feeding plan updates')
def _(context):
    feeding_plan_page = FeedingPage(context)
    feeding_plan_page.next_button.click()


@then('Redirected to wet food selection page')
def _(context):
    feeding_plan_page = FeedingPage(context)
    assert feeding_plan_page.notification_banner.is_displayed()
