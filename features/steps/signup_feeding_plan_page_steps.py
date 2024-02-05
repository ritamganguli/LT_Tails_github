from behave import when, then, use_step_matcher
import time
from features.page_objects.navigation_page import NavigationPage
from features.page_objects.feeding_plan_page import FeedingPlanPage
from features.page_objects.paypal_page import PaypalPage
from features.page_objects.project_box_pages import ProjectBoxPages

use_step_matcher("re")


@then('Dry food and treats page excluded health issue "(.*)" ingredients "(.*)"')
def _(context, health, excluded):
    # dry page
    time.sleep(20)
    box_page = ProjectBoxPages(context)
    box_page.dry_ingredients.click()
    feeding_plan = FeedingPlanPage(context)
    text = feeding_plan.claims.text
    contains = text
    assert health not in contains
    box_page.add_to_box_button.click()
    time.sleep(10)


@then('Dry food and treats page excluded ingredients "(.*)"')
def _(context, excluded_):
    # dry page
    box_page = ProjectBoxPages(context)
    time.sleep(15)
    feeding_plan = FeedingPlanPage(context)
    text = feeding_plan.claims.text
    contains = text
    assert excluded_ in contains
    box_page.dry_add_to_box_button.click()

    # treats
    treats_page = ProjectBoxPages(context)
    time.sleep(10)
    treats_page.scroll_down_page()
    time.sleep(10)
    treats_page.go_to_box_button.click()


@then('Treats page excluded ingredients "(.*)"')
def _(context, health_item):
    # dry page
    box_page = ProjectBoxPages(context)
    time.sleep(15)
    feeding_plan = FeedingPlanPage(context)
    text = feeding_plan.claims.text
    contains = text
    assert health_item not in contains
    box_page.add_to_box_button.click()
    time.sleep(10)


@then('Dry and treats page excluded ingredients "(.*)"')
def step_impl(context, ingredients):
    # dry page
    box_page = ProjectBoxPages(context)
    time.sleep(15)
    feeding_plan = FeedingPlanPage(context)
    text = feeding_plan.claims.text
    contains = text
    assert ingredients in contains
    box_page.dry_add_to_box_button.click()
    time.sleep(10)

    # treats
    treats_page = ProjectBoxPages(context)
    time.sleep(7)
    text = feeding_plan.claims.text
    contains = text
    assert ingredients in contains
    treats_page.scroll_down_page()
    time.sleep(3)
    treats_page.go_to_box_button.click()
    time.sleep(5)


@then('Feeding plan page netherlands excluded ingredients "(.*)"')
def _(context, excluded):
    feeding_plan = FeedingPlanPage(context)

    text = feeding_plan.nl_contains_no_ingredients.text.strip()
    contains_no = text.split(":")[-1].strip()
    assert contains_no == excluded
    feeding_plan.next_feeding_plan.click()


@then('Feeding plan page german excluded ingredients "(.*)"')
def _(context, excluded):
    feeding_plan = FeedingPlanPage(context)

    text = feeding_plan.gr_contains_no.text.strip()
    contains_no = text.split(":")[-1].strip()
    assert contains_no == excluded
    feeding_plan.next_feeding_plan.click()


@then('Feeding plan page display designed for and contains no "(.*)"')
def _(context, contains_no):
    feeding_plan = FeedingPlanPage(context)
    time.sleep(5)
    text = feeding_plan.contains_no.text.strip()
    designed = text.split(":")[-1].strip()
    assert designed == contains_no
    feeding_plan.next_feeding_plan.click()
    time.sleep(5)


@then('Feeding plan page netherlands display designed for and contains no "(.*)"')
def _(context, contains_no):
    feeding_plan = FeedingPlanPage(context)
    time.sleep(10)
    text = feeding_plan.nl_contains_no.text.strip()
    designed = text.split(":")[-1].strip()
    assert designed == contains_no
    feeding_plan.next_feeding_plan.click()


@then('Feeding plan page display german designed to support "(.*)"')
def _(context, german_health_issues):
    feeding_plan = FeedingPlanPage(context)
    time.sleep(20)
    designed = feeding_plan.de_designed_support
    assert designed.text == german_health_issues
    feeding_plan.next_feeding_plan.click()


@then('Feeding plan page display designed to support "(.*)"')
def _(context, health_issues):
    feeding_plan = FeedingPlanPage(context)
    time.sleep(10)
    health = feeding_plan.designed_support
    assert health.text == health_issues
    feeding_plan.next_feeding_plan.click()


@then('Feeding plan page netherlands display designed to support "(.*)"')
def _(context, health_issues):
    feeding_plan = FeedingPlanPage(context)
    time.sleep(10)
    health = feeding_plan.nl_designed_support
    assert health.text == health_issues
    feeding_plan.next_feeding_plan.click()


@then('Feeding plan page france display designed to support "(.*)"')
def _(context, health_issues):
    feeding_plan = FeedingPlanPage(context)
    time.sleep(20)
    designed = feeding_plan.fr_designed_support
    assert designed.text == health_issues
    feeding_plan.next_feeding_plan.click()


@then('Feeding plan page display german designed for and contains no "(.*)"')
def _(context, contains_no_):
    feeding_plan = FeedingPlanPage(context)
    time.sleep(20)
    text = feeding_plan.gr_contains_no.text.strip()
    contains_not = text.split(":")[-1].strip()
    assert contains_not == contains_no_
    feeding_plan.next_feeding_plan.click()


@then('Feeding plan page france display designed for and contains no "(.*)"')
def _(context, contains_no):
    feeding_plan = FeedingPlanPage(context)
    time.sleep(20)
    text = feeding_plan.fr_contains_no.text.strip()
    no_contains = text.split(":")[-1].strip()
    assert no_contains == contains_no
    feeding_plan.next_feeding_plan.click()


@then('Feeding plan page with no option "(.*)" to select wet food or treats')
def _(context, no_option):
    feeding_plan = FeedingPlanPage(context)

    text = feeding_plan.contains_no.text.strip()
    contains_not = text.split(":")[-1].strip()
    assert no_option in contains_not
    feeding_plan.next_feeding_plan.click()


@then('Feeding plan page netherlands with no option "(.*)" to select wet food or treats')
def _(context, no_option):
    feeding_plan = FeedingPlanPage(context)

    text = feeding_plan.nl_contains_no_ingredients.text.strip()
    contains_not = text.split(":")[-1].strip()
    assert contains_not == no_option
    feeding_plan.next_feeding_plan.click()


@when('Dry food box page contains "(.*)" to select wet food or treats')
def _(context, no_option):
    feeding_plan = FeedingPlanPage(context)

    # dry page
    box_page = ProjectBoxPages(context)
    time.sleep(10)
    text = feeding_plan.claims.text
    contains = text
    assert no_option in contains
    box_page.dry_add_to_box_button.click()
    time.sleep(10)

    # wet page
    time.sleep(2)
    box_page.choose_this_selection_button.click()
    time.sleep(10)

    # treats page
    treats_page = ProjectBoxPages(context)
    time.sleep(3)
    treats_page.scroll_down_page()
    time.sleep(3)
    treats_page.go_to_box_button.click()
    time.sleep(5)


@when("Feeding plan continue box")
def _(context):
    feeding_plan = FeedingPlanPage(context)
    time.sleep(5)
    feeding_plan.scroll_to_bottom_of_page()
    time.sleep(20)
    feeding_plan.next_feeding_plan.click()

    # treats page
    treats_page = ProjectBoxPages(context)
    time.sleep(3)
    treats_page.scroll_down_page()
    time.sleep(3)
    treats_page.go_to_box_button.click()
    time.sleep(5)


@when("Feeding plan continue")
def _(context):
    feeding_plan = FeedingPlanPage(context)
    time.sleep(15)
    feeding_plan.scroll_to_bottom_of_page()
    time.sleep(5)
    feeding_plan.next_feeding_plan.click()


@then('Feeding plan page with no german option "(.*)" to select wet food or treats')
def _(context, no_option):
    feeding_plan = FeedingPlanPage(context)

    text = feeding_plan.gr_contains_no.text.strip()
    contains_not = text.split(":")[-1].strip()
    assert contains_not == no_option
    feeding_plan.next_feeding_plan.click()


@when("Add another dog from feeding plan page")
def _(context):
    feeding_page = FeedingPlanPage(context)
    navigate = NavigationPage(context)
    navigate.scroll_to_bottom_of_page()
    time.sleep(10)
    feeding_page.another_dog.click()
    time.sleep(10)
    navigate.pets_another_dog.click()


@when("Add another dog from feeding plan page netherlands")
def _(context):
    feeding_page = FeedingPlanPage(context)
    navigate = NavigationPage(context)
    navigate.scroll_to_bottom_of_page()
    time.sleep(10)
    feeding_page.nl_another_dog.click()
    time.sleep(10)
    navigate.pets_another_dog.click()


@then('Add another dog from feeding plan page "(.*)"')
def _(context, feedingplan):
    feeding_page = FeedingPlanPage(context)
    navigate = NavigationPage(context)
    time.sleep(20)
    feeding_page.another_dog.click()
    time.sleep(20)
    dog = navigate.another_dog_link
    assert dog.text == feedingplan


@when('Add another dog from feeding plan page "(.*)"')
def _(context, country_for):
    feeding_page = FeedingPlanPage(context)
    navigate = NavigationPage(context)
    time.sleep(10)
    navigate.scroll_to_bottom_of_page()
    time.sleep(5)
    if country_for == "France":
        feeding_page.fr_another_dog.click()
    if country_for == "Austria":
        feeding_page.de_another_dog.click()
    if country_for == "Germany":
        feeding_page.de_another_dog.click()
    time.sleep(10)
    navigate.pets_another_dog.click()


@when("Feeding plan continue with paypal")
def _(context):
    paypal_page = PaypalPage(context)
    time.sleep(5)
    paypal_page.paypal_option.click()
    paypal_page.paypal_button.click()


@when('Confirm dental dailies displays on feeding plan page')
def _(context):
    feeding_plan_page = FeedingPlanPage(context)
    assert feeding_plan_page.feeding_plan_summary.text() == 'Dental dailies'


@then("Feeding plan display")
def _(context):
    feeding_plan = FeedingPlanPage(context)
    time.sleep(15)
    feeding_plan.next_feeding_plan.click()


@then('Dry food page display tailored to needs "(.*)"')
def _(context, health_item):
    # dry page
    box_page = ProjectBoxPages(context)
    time.sleep(15)
    feeding_plan = FeedingPlanPage(context)
    text = feeding_plan.claims.text
    contains = text
    assert health_item in contains
    box_page.dry_add_to_box_button.click()
    time.sleep(10)


@when('Dry food page display tailored to needs "(.*)"')
def _(context, health_item):
    # dry page
    time.sleep(20)
    feeding_plan = FeedingPlanPage(context)
    text = feeding_plan.claims_health(health_item).text
    contains = text
    assert health_item in contains
