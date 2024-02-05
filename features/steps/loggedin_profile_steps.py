from behave import when, then, use_step_matcher
import time

from selenium.webdriver import ActionChains

from features.page_objects.dashboard_page import DashboardPage
from features.page_objects.profile_loggedin_page import ProfilePage


use_step_matcher("re")


@when('Navigate to pet profile page')
def _(context):
    dashboard_page = DashboardPage(context)
    time.sleep(5)
    dashboard_page.hamburger_menu.click()

    dashboard_page.profile_page_select.click()

    assert ProfilePage(context).view_feeding_plan_cta.is_displayed()


@then('Successful update notification "(.*)" is displayed on profile page')
def _(context, notification):
    profile_page = ProfilePage(context)
    confirmation = profile_page.profile_notification

    assert notification in confirmation.text


# endregion

# region Flow final step: Confirm feeding plan changes

@when("Confirm feeding plan changes")
def _(context):
    profile_page = ProfilePage(context)
    time.sleep(7)
    assert profile_page.feeding_plan_header.text == "Confirm new feeding plan"
    context.browser.execute_script("window.scrollBy(0,400);")
    # actions = ActionChains(profile_page.browser)
    # element = profile_page.confirm_button
    # actions.move_to_element(element).click(element).perform()
    time.sleep(7)
    profile_page.confirm_button.click()

    assert profile_page.view_feeding_plan_cta.is_displayed()


@when("Update weight and condition")
def _(context):
    profile_page = ProfilePage(context)

    time.sleep(5)
    context.browser.execute_script("window.scrollBy(0,500);")
    profile_page.update_weight.click()

    assert profile_page.weight_header.is_displayed()

    profile_page.weight_input.clear()
    profile_page.weight_input.send_keys(20)
    profile_page.next_button.click()
    time.sleep(3)
    assert profile_page.condition_header.is_displayed()

    profile_page.next_button.click()


# endregion

# region Flow: Add health condition


@when('Add health condition "(.*)"')
def _(context, health_condition):
    profile_page = ProfilePage(context)

    time.sleep(10)
    context.browser.execute_script("window.scrollBy(0,500);")
    profile_page.update_condition.click()

    if health_condition.lower() == "joints":
        profile_page.joints.click()
    if health_condition.lower() == "skin and coat":
        profile_page.skin_coat.click()
    if health_condition.lower() == "digestion":
        profile_page.digestion.click()
    if health_condition.lower() == "pancreatitis":
        # scroll required on mobile view
        profile_page.pancreatitis.click()

    # profile_page.scroll_down_page()
    time.sleep(2)
    context.browser.execute_script("window.scrollBy(0,200);")
    time.sleep(2)
    profile_page.continue_button.click()


# endregion

# region Flow: Add exclusions


@when('Add ingredient to exclude "(.*)"')
def _(context, ingredient):
    profile_page = ProfilePage(context)
    context.browser.execute_script("window.scrollBy(0,300);")
    time.sleep(1)
    profile_page.add_exclusion.click()
    header = profile_page.exclusion_header

    assert "Select the ingredients" in header.text

    if ingredient.lower() == "chicken":
        profile_page.chicken_exclusion.click()
    if ingredient.lower() == "beef":
        profile_page.beef_exclusion.click()
    if ingredient.lower() == "lamb":
        profile_page.lamb_exclusion.click()
    if ingredient.lower() == "fish":
        profile_page.fish_exclusion.click()
    if ingredient.lower() == "wheat":
        profile_page.wheat_exclusion.click()
    if ingredient.lower() == "grain":
        profile_page.grain_exclusion.click()
    if ingredient.lower() == "hypoallergenic":
        profile_page.hypoallergenic_exclusion.click()

    context.browser.execute_script("window.scrollBy(0,200);")
    profile_page.continue_button.click()


# endregion
