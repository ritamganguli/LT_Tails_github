from behave import given, when, then, use_step_matcher

import time
from features.page_objects.home_page import HomePage
from features.page_objects.current_diet_page import CurrentDietPage
from features.page_objects.checkout_address_page import CheckoutAddressPage
from features.page_objects.current_food_page import CurrentFoodPage
from features.page_objects.email_page import EmailPage
from features.page_objects.motivation_page import MotivationPage
from features.page_objects.mydog_page import MydogPage
from features.page_objects.breed_page import BreedPage
from features.page_objects.payment_page import PaymentPage
from features.page_objects.pricing_page import PricingPage
from features.page_objects.weight_page import WeightPage
from features.page_objects.activity_page import ActivityPage
from features.page_objects.health_Ingredients_page import HealthIngredientsPage
from features.page_objects.dashboard_page import DashboardPage
from features.page_objects.navigation_page import NavigationPage
from selenium.webdriver.common.keys import Keys
from features.page_objects.project_box_pages import ProjectBoxPages
from features.page_objects.deliveries_page import DeliveriesPage
from lighthouse_performance.lighthouse_report import LighthouseReport
from lighthouse_performance.lighthouse_audit import LighthouseAudit
from lighthouse_performance.lighthouse_avg_audit import LighthouseAvgAudit

import uuid
import string
from random import choice
from selenium.webdriver.common.action_chains import ActionChains

use_step_matcher("re")


@when('Add "(.*)" information age "(.*)" year neutered purebreed "(.*)" lighthouse "(.*)"')
def _(context, dogn, yr, pure_breed_, audit):
    dog = MydogPage(context)
    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(7)

    short_random = uuid.uuid4()
    random = str(short_random)[:7]
    time.sleep(10)
    dog_form = dog.dog_form
    dog.name_input.send_keys(
        "behave" + random,
    )

    dog.years_input.send_keys(yr)
    dog.male_input.click()
    dog_form.submit()

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(7)

    breed = BreedPage(context)
    time.sleep(7)
    breed_form = breed.breed_form
    time.sleep(5)
    breed.purebreed_input.click()
    time.sleep(5)
    breed.breed_search.send_keys(pure_breed_)
    time.sleep(5)
    breed.breed_search.send_keys(Keys.DOWN)

    breed_form.submit()


@when('Select gain weight motivation for dog food lighthouse "(.*)"')
def _(context, audit):
    motivation_page = MotivationPage(context)
    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()

    time.sleep(15)

    motivation = motivation_page.motivation_form
    motivation_page.gain_weight.click()
    motivation.submit()
    time.sleep(1)

    motivation_info = motivation_page.motivation_info_form
    motivation_info.submit()


@when('performance status no working dog weight "(.*)" and lighthouse "(.*)"')
def _(context, number, audit):
    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()

    time.sleep(15)
    weight = WeightPage(context)
    weight_form = weight.weight_form
    weight.weight_input.send_keys(number)
    weight.gain_little_weight.click()
    weight_form.submit()

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()

    time.sleep(15)

    weight = WeightPage(context)
    underweight_info = weight.underweight_info_form
    underweight_info.submit()

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()

    time.sleep(20)

    activity_page = ActivityPage(context)
    activity_form = activity_page.activity_form
    activity_form.submit()


@when('Health Ingredients no issues lighthouse "(.*)"')
def _(context, audit):
    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()

    time.sleep(15)
    health_ingredients = HealthIngredientsPage(context)
    health = health_ingredients.health_form
    health.submit()

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()

    time.sleep(20)

    exclusions = health_ingredients.exclusions_form_uk
    health_ingredients.no_exclusions.click()
    exclusions.submit()


@when('performance current food dry "(.*)" selected wet "(.*)" lighthouse "(.*)"')
def _(context, drybrand, wet, audit):
    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()

    time.sleep(15)
    current_food = CurrentFoodPage(context)
    current_food_form = current_food.current_food_form
    current_food.no_dryfood_brand.click()
    time.sleep(5)
    if wet == "Mini can (156g)":
        current_food.current_wet.click()

    time.sleep(5)
    current_food_form.submit()


@when('Select flavour anything lighthouse "(.*)"')
def _(context, audit):
    current_flavour = CurrentFoodPage(context)
    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(15)

    flavours_form = current_flavour.flavours_form
    time.sleep(7)
    flavours_form.submit()


@when('Complete email page lighthouse "(.*)"')
def _(context, audit):
    email = EmailPage(context)
    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(15)

    email_form = email.email_form
    chars = string.digits
    random = ''.join(choice(chars) for _ in range(6))
    email.email_input.send_keys("audit" + random + "@example.com")
    time.sleep(3)
    email.opt_in_no.click()
    email.opt_in_yes.click()
    email.opt_in_no.click()
    email_form.submit()


@when('performance select dry and wet Project Box lighthouse "(.*)"')
def _(context, audit):
    # land on core diet page but go through to wet food link first
    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(30)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(30)

    box_page = ProjectBoxPages(context)
    box_page.see_wet_food.click()

    # run lighthouse audits
    time.sleep(20)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(30)

    # back to core diet page
    box_page = ProjectBoxPages(context)
    box_page.choose_this_selection_button.click()
    time.sleep(20)

    # core diet to treats via CTA
    box_page.add_to_box_button.click()

    # run lighthouse audits
    time.sleep(10)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(30)


@when('Pricing continue with card lighthouse "(.*)"')
def _(context, audit):
    pricing = PricingPage(context)
    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(20)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(15)

    pricing.card_option.click()
    pricing.submit_pricing.click()


@when('Checkout address postcode "(.*)" express delivery date lighthouse "(.*)"')
def _(context, pcodeuk, audit):
    address = CheckoutAddressPage(context)
    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()

    time.sleep(15)

    address.first_name.send_keys("qatest")
    address.last_name.send_keys("qatest")
    address.password.send_keys("password1234")
    address.opt_out_phone.click()
    address.opt_out_text.click()
    time.sleep(10)

    address.opt_out_text.send_keys(Keys.TAB * 3)

    actions = ActionChains(address.browser)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    time.sleep(10)

    address.search_postcode.send_keys(pcodeuk)
    time.sleep(5)
    address.postcode_lookup.click()
    time.sleep(5)
    address.address_select_uk()
    address.opt_in_email.click()
    time.sleep(7)
    address.get_dates.click()
    time.sleep(30)

    address.opt_in_email.send_keys(Keys.TAB * 6)

    actions = ActionChains(address.browser)
    actions.send_keys(Keys.ENTER)
    actions.perform()


@when('Select no treats Project Box lighthouse "(.*)"')
def _(context, audit):
    treats_page = ProjectBoxPages(context)

    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()

    time.sleep(15)
    treats_page.go_to_box_button.click()
    time.sleep(10)


@when('Checkout with stripe payment details lighthouse (.*)')
def _(context, audit):
    payment = PaymentPage(context)
    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()

    time.sleep(15)
    payment.checkout_stripe_payment_not_checking_error()


@then('Signup completed and "(.*)" display lighthouse "(.*)"')
def _(context, my_dashboard, audit):
    signup_complete = DashboardPage(context)

    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(20)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()

    time.sleep(15)
    signup_complete.continue_dashboard.click()


@when('Complete email page for prod lighthouse "(.*)"')
def _(context, audit):
    email = EmailPage(context)

    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(25)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()

    time.sleep(40)
    email_form = email.email_form

    email.create_random_email_prod()
    email.opt_in_no.click()
    email.scroll_to_bottom_of_page()
    email_form.submit()


@then('Navigate to each dashboard page lighthouse "(.*)"')
def _(context, audit):
    dashboard = DashboardPage(context)
    navigation = NavigationPage(context)

    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    time.sleep(15)
    navigation.home_menu.click()
    time.sleep(8)
    dashboard.treatment_page.click()
    time.sleep(6)

    time.sleep(5)
    navigation.home_menu.click()
    time.sleep(5)
    dashboard.treatment_page.click()

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(15)

    navigation.home_menu.click()
    time.sleep(8)
    dashboard.feeding_plan_page_select.click()
    # DashboardPage(context).dashboard_feed_better_service_dismiss()
    time.sleep(5)

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(15)

    navigation.home_menu.click()
    time.sleep(8)
    dashboard.deliveries_page_select.click()
    time.sleep(6)

    # run lighthouse audits
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(15)

    navigation.home_menu.click()
    time.sleep(8)
    dashboard.raf_page_select.click()

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(15)

    navigation.home_menu.click()
    time.sleep(8)
    dashboard.account_page_select.click()

    # run lighthouse audits
    time.sleep(5)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(15)

    navigation.home_menu.click()
    time.sleep(8)
    dashboard.dashboard_page_select.click()

    # run lighthouse audits
    time.sleep(5)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(15)

    time.sleep(2)
    navigation.home_menu.click()
    time.sleep(8)
    dashboard.profile_page_select.click()
    time.sleep(5)

    navigation.home_menu.click()
    time.sleep(8)
    dashboard.shop_page_select.click()

    # run lighthouse audits
    time.sleep(25)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(15)


@when('Current diet select dry wet food and treats other food lighthouse "(.*)"')
def _(context, audit):
    current = CurrentDietPage(context)
    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(10)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(15)

    current_form = current.current_diet_form
    current.current_dryfood.click()
    current.current_drywet.click()
    current.current_otherfood.click()
    current_form.submit()


@when('navigate into signup flow in "(.*)" country prod lighthouse "(.*)"')
def _(context, country, audit):
    home_page = HomePage(context)

    time.sleep(7)
    home_page.warning_close_cookie()
    time.sleep(5)
    home_page.try_now.click()


@given('on homepage and "(.*)" country lighthouses')
def _(context, country):
    home_page = HomePage(context)
    home_page.goto("/")

    for cookie in context.browser.cookies_to_set_pb:
        context.browser.add_cookie(cookie)

    time.sleep(5)

    home_page.try_now.click()
    home_page.country.click()
    time.sleep(5)
    home_page.select_country(country)
    submit = home_page.country_submit
    submit.click()


@given('on homepage and "(.*)" country lighthouse "(.*)"')
def _(context, country, audit):
    home_page = HomePage(context)
    home_page.goto("/")

    for cookie in context.browser.cookies_to_set_pb:
        context.browser.add_cookie(cookie)

    time.sleep(5)

    home_page.try_now.click()
    home_page.country.click()
    time.sleep(5)
    home_page.select_country(country)
    submit = home_page.country_submit
    submit.click()


@given('Logged in to "(.*)" customer account "(.*)" email')
def _(context, country, email_):
    home_page = HomePage(context)
    email_page = EmailPage(context)

    home_page.goto("/")
    navigation = NavigationPage(context)
    email = EmailPage(context)

    customer_email = email_

    for cookie in context.browser.cookies_to_set:
        context.browser.add_cookie(cookie)

    home_page.country_select_login(country)
    email_page.country_for_login(country)
    email.email_login.send_keys(customer_email)
    email.password_dashboard_login.send_keys(1234)
    context.email = customer_email
    navigation.account_login.click()


@given('Logged in to "(.*)" customer account "(.*)" email prod')
def _(context, country, email_):
    dashboard_page = DashboardPage(context)
    home_page = HomePage(context)
    email = EmailPage(context)
    home_page.goto_prod_signin()
    home_page.warning_close_cookie()

    navigation = NavigationPage(context)

    email.email_login.send_keys(email_)
    email.password_dashboard_login.send_keys("Password1234")
    navigation.account_login.click()

    dashboard_page.wait_for_new_account_loading_animation_to_disappear()
    # dashboard_page.dashboard_feed_survey_dismiss()
    time.sleep(5)


@when('Checkout address postcode "(.*)" express delivery date prod lighthouse "(.*)"')
def _(context, pcodeuk, audit):
    address = CheckoutAddressPage(context)
    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(15)

    address.first_name.send_keys("qatest")
    address.last_name.send_keys("qatest")
    address.password.send_keys("password1234")
    address.opt_out_phone.click()
    address.opt_out_text.click()
    time.sleep(10)

    address.opt_out_text.send_keys(Keys.TAB * 3)

    actions = ActionChains(address.browser)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    time.sleep(10)

    address.search_postcode.send_keys(pcodeuk)
    time.sleep(5)
    address.postcode_lookup.click()
    time.sleep(5)
    address.address_select_uk_prod()
    address.opt_in_email.click()
    time.sleep(7)
    address.get_dates.click()
    time.sleep(10)

    address.opt_in_email.send_keys(Keys.TAB * 6)

    actions = ActionChains(address.browser)
    actions.send_keys(Keys.ENTER)
    actions.perform()


@then('Checkout with stripe payment details prod lighthouse "(.*)"')
def _(context, audit):
    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(15)


@then('Performance check shop page load for "(.*)" products lighthouse "(.*)"')
def _(context, recommend, audit):
    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(15)

    navigation = NavigationPage(context)
    dashboard = DashboardPage(context)
    navigation.home_menu.click()
    dashboard.shop_page_select.click()
    time.sleep(20)

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(15)


@when('View full delivery details lighthouse "(.*)"')
def _(context, audit):
    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(15)
    deliveries_page = DeliveriesPage(context)
    deliveries_page.view_delivery_button.click()

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(15)


@when('Performance select deliveries page displays lighthouse "(.*)"')
def _(context, audit):
    dashboard_page = DashboardPage(context)
    dashboard_page.hamburger_menu.click()
    dashboard_page.deliveries_page_select.click()

    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(15)


@then('Performance view full delivery details lighthouse "(.*)"')
def _(context, audit):
    deliveries_page = DeliveriesPage(context)
    deliveries_page.view_delivery_button.click()

    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()
    time.sleep(15)


@given('Logged in to PROD "(.*)" customer account "(.*)" and password "(.*)" lighthouse')
def _(context, country, account, password):
    dashboard_page = DashboardPage(context)
    home_page = HomePage(context)

    email = EmailPage(context)
    home_page.goto_prod_signin()

    home_page.warning_close_cookie()
    navigation = NavigationPage(context)

    email.email_login.send_keys(account)
    email.password_dashboard_login.send_keys(password)
    navigation.account_login.click()

    dashboard_page.wait_for_new_account_loading_animation_to_disappear()
    # dashboard_page.dashboard_feed_survey_dismiss()
    time.sleep(5)

    for cookie in context.browser.cookies_to_set:
        context.browser.add_cookie(cookie)


@when('Performance current food dry "(.*)" selected wet "Mini can (.*)" lighthouse "(.*)" prod')
# @then('Performance current food dry "(.*)" selected wet "Mini can "(.*)" lighthouse "(.*)" prod')
def _(context, drybrand, wet, audit):
    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()

    time.sleep(15)
    current_food = CurrentFoodPage(context)
    current_food_form = current_food.current_food_form
    current_food.no_dryfood_brand.click()
    time.sleep(5)
    if wet == "Mini can (156g)":
        current_food.current_wet.click()

    time.sleep(5)
    current_food_form.submit()


@when('lighthouse current food dry "(.*)" selected wet "(.*)" lighthouse "(.*)"')
def _(context, drybrand, wet, audit):
    light = LighthouseReport(context)
    light_export = LighthouseAudit(context)
    light_avg = LighthouseAvgAudit(context)

    # run lighthouse audits
    time.sleep(7)
    if audit == "audit":
        light_export.run_audit()
    if audit == "avg audit":
        light_avg.run_audit(7, 7, 5.8, 100)
    if audit == "report":
        light.run_report()

    time.sleep(15)
    current_food = CurrentFoodPage(context)
    current_food_form = current_food.current_food_form
    current_food.no_dryfood_brand.click()
    time.sleep(5)
    if wet == "Mini can (156g)":
        current_food.current_wet.click()

    time.sleep(5)
    current_food_form.submit()


@given('Logged in to "United Kingdom" customer account "(.*)" email and password "(.*)"')
def _(context, country, email_):
    home_page = HomePage(context)
    email_page = EmailPage(context)

    home_page.goto("/")
    navigation = NavigationPage(context)
    email = EmailPage(context)

    customer_email = email_

    for cookie in context.browser.cookies_to_set:
        context.browser.add_cookie(cookie)

    home_page.country_select_login(country)
    email_page.country_for_login(country)
    email.email_login.send_keys(customer_email)
    email.password_dashboard_login.send_keys("Passwordonetwo")
    context.email = customer_email
    navigation.account_login.click()