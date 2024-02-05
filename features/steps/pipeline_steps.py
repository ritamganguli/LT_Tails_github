from behave import given, when, then, use_step_matcher
import time

from features.page_objects.home_page import HomePage
from features.page_objects.current_diet_page import CurrentDietPage
from features.page_objects.checkout_address_page import CheckoutAddressPage
from features.page_objects.current_food_page import CurrentFoodPage
from features.page_objects.email_page import EmailPage
from features.page_objects.feeding_plan_page import FeedingPlanPage
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
from features.page_objects.new_food_page import NewFoodPage
from features.data_seed.provider_state_seeds import *
from selenium.webdriver.common.keys import Keys
import uuid

from selenium.webdriver.common.action_chains import ActionChains

use_step_matcher("re")


@given('on homepage and "(.*)" country pipeline')
def _(context, country):
    home_page = HomePage(context)
    home_page.goto("/")

    for cookie in context.browser.cookies_to_set_pb:
        context.browser.add_cookie(cookie)

    home_page.try_now.click()
    home_page.country.click()

    home_page.select_country(country)
    submit = home_page.country_submit
    submit.click()


@when('Add "(.*)" information age "(.*)" years neutered purebreed "(.*)" pipeline')
def _(context, dogn, yr, pure_breed_):
    dog = MydogPage(context)
    short_random = uuid.uuid4()
    random = str(short_random)[:7]
    time.sleep(5)

    dog.name_input.send_keys(
        "behave" + random,
    )

    time.sleep(7)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   dog.male_input)

    dog.male_input.click()
    dog.years_input.send_keys(yr)

    # time.sleep(3)
    # # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # # zendesk widget doesn't intercept the click into update condition
    # context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
    #                                dog.dog_form)
    # dog.dog_form.click()

    dog_form = dog.dog_form
    dog_form.submit()

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


@when("Select gain weight motivation for dog food pipeline")
def _(context):
    motivation_page = MotivationPage(context)

    motivation = motivation_page.motivation_form
    motivation_page.gain_weight.click()
    motivation.submit()

    motivation_info = motivation_page.motivation_info_form
    motivation_info.submit()


@when('Status no working dog weight "(.*)" pipeline')
def _(context, number):
    weight = WeightPage(context)
    weight_form = weight.weight_form
    weight.weight_input.send_keys(number)
    weight.gain_little_weight.click()
    weight_form.submit()

    underweight_info = weight.underweight_info_form
    underweight_info.submit()

    activity_page = ActivityPage(context)
    activity_form = activity_page.activity_form
    activity_form.submit()


@when("Health Ingredients no issues pipeline")
def _(context):
    health_ingredients = HealthIngredientsPage(context)
    health = health_ingredients.health_form
    health.submit()

    exclusions = health_ingredients.exclusions_form_uk
    health_ingredients.no_exclusions.click()
    exclusions.submit()


@when("Health Ingredients no issues international pipeline")
def _(context):
    health_ingredients = HealthIngredientsPage(context)
    time.sleep(5)
    health = health_ingredients.health_form
    health.submit()

    health_ingredients.no_exclusions_inter.click()
    health_ingredients.exclusions_next_inter.click()


@when("Current diet select dry and wet food pipeline")
def _(context):

    current = CurrentDietPage(context)
    time.sleep(10)
    current_form = current.current_diet_form
    current.current_dryfood.click()
    current.current_drywet.click()
    current_form.submit()


@when('Current food dry "(.*)" selected wet "(.*)" pipeline')
def _(context, drybrand, wet):
    time.sleep(5)
    current_food = CurrentFoodPage(context)

    current_food_form = current_food.current_food_form
    current_food.no_dryfood_brand.click()

    if wet == "Mini can (156g)":
        current_food.current_wet.click()
    if wet == "Mini conserve (156g)":
        current_food.current_wet_france.click()
    if wet == "Kleine Dose (156g)":
        current_food.current_wet_germany.click()

    current_food_form.submit()


@when("Select flavour anything pipeline")
def _(context):
    current_flavour = CurrentFoodPage(context)

    flavours_form = current_flavour.flavours_form

    flavours_form.submit()


@when("Complete email page pipeline")
def _(context):
    email = EmailPage(context)

    email_form = email.email_form

    # random = ''.join(choice(chars) for _ in range(7))
    random = email.strong_randomise_email()
    email.email_input.send_keys(random)

    time.sleep(5)
    email.opt_in_no.click()
    email.opt_in_yes.click()
    email.opt_in_no.click()
    email_form.submit()


@when("Feeding plan continue pipeline")
def _(context):
    feeding_plan = FeedingPlanPage(context)

    feeding_plan.next_feeding_plan_nl.click()


@when("Pricing continue with card pipeline")
def _(context, ):
    pricing = PricingPage(context)
    time.sleep(20)
    pricing.card_option.click()
    pricing.submit_pricing.click()


@when('Checkout address postcode "(.*)" express delivery date pipeline')
def _(context, pcodeuk):
    address = CheckoutAddressPage(context)
    time.sleep(7)
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

    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   address.postcode_lookup)
    address.postcode_lookup.click()
    time.sleep(5)
    address.address_select_uk()
    address.opt_in_email.click()
    time.sleep(7)
    address.get_dates.click()
    time.sleep(10)

    address.opt_in_email.send_keys(Keys.TAB * 6)

    actions = ActionChains(address.browser)
    actions.send_keys(Keys.ENTER)
    actions.perform()


@when('Checkout manual address "(.*)" and "(.*)" "(.*)" express delivery date pipeline')
def _(context, first_line, city, post_code):
    address = CheckoutAddressPage(context)
    nav = NavigationPage(context)
    time.sleep(7)
    address.first_name.send_keys("qatest")
    address.last_name.send_keys("qatest")
    address.password.send_keys("password1234")
    address.opt_out_phone.click()
    address.opt_out_text.click()
    time.sleep(5)
    address.address_next.click()
    time.sleep(5)

    address.search_postcode.send_keys(post_code)
    time.sleep(7)
    nav.dismiss_keyboard()
    address.postcode_lookup.click()

    time.sleep(7)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    context.browser.execute_script("window.scrollBy(0,600);")
    address.opt_in_email.click()
    context.browser.execute_script("window.scrollBy(0,200);")
    time.sleep(3)
    address.get_dates.click()
    time.sleep(5)
    address.generic_address_next.click()

    time.sleep(10)
    address.first_line.send_keys(first_line)
    address.man_post_code.send_keys(post_code)
    address.man_city.send_keys(city)
    address.opt_in_email.click()
    address.get_dates.click()

    time.sleep(6)
    address.opt_in_email.send_keys(Keys.TAB * 6)

    address.generic_address_next.click()


@when("New Food Dry and Wet Food pipeline")
def _(context):
    new_food = NewFoodPage(context)
    time.sleep(6)
    feeding = new_food.feeding_preference_form
    new_food.feeding_pref_dry_wet.click()
    feeding.submit()


@when("Checkout address for France future delivery date pipeline")
def _(context):
    address = CheckoutAddressPage(context)
    address.first_name.send_keys("qatest")
    address.last_name.send_keys("qatest")
    address.password.send_keys("password1234")
    time.sleep(1)
    address.opt_out_phone.click()
    address.opt_out_text.click()
    time.sleep(5)
    address.next_page()
    address.address_france()
    address.opt_in_email.click()
    time.sleep(5)
    address.fr_get_dates.click()
    address.next_page()
    time.sleep(10)


@then("Checkout with stripe payment details pipeline")
def _(context):
    payment = PaymentPage(context)
    payment.checkout_stripe_payment()


@when("Checkout with stripe payment details pipeline")
def _(context):
    payment = PaymentPage(context)
    payment.checkout_stripe_payment_not_checking_error()


@when("Checkout with stripe payment details pipeline DE")
def _(context):
    payment = PaymentPage(context)
    payment.checkout_stripe_payment_not_checking_error()


@when("Checkout address for France express delivery pipeline")
def _(context):
    address = CheckoutAddressPage(context)
    address.first_name.send_keys("qatest")

    address.first_name.send_keys("qatest")
    address.last_name.send_keys("qatest")
    address.password.send_keys("password1234")
    address.opt_out_phone.click()
    address.opt_out_text.click()
    address.address_next.click()

    address.address_france()
    address.opt_in_email.click()
    address.opt_in_email.send_keys(Keys.TAB * 1)
    address.get_dates.click()
    address.following_dates_selection_page.click()


@when('Checkout international address for Germany express delivery pipeline')
def _(context):
    address = CheckoutAddressPage(context)
    address.first_name.send_keys("qatest")
    address.last_name.send_keys("qatest")
    address.password.send_keys("password1234")
    time.sleep(1)
    address.opt_out_phone.click()
    address.opt_out_text.click()
    time.sleep(5)
    address.address_next.click()

    # Your address
    time.sleep(5)
    address.add_address_for_country("Germany")
    address.opt_in_email.click()

    address.scroll_down_page()
    time.sleep(10)
    address.get_dates_de.click()
    time.sleep(2)
    context.browser.execute_script("window.scrollBy(0,200);")
    address.address_next.click()


@when("Pricing continue with gocardless pipeline")
def _(context):
    pricing = PricingPage(context)
    nav = NavigationPage(context)

    time.sleep(5)
    nav.check_height_page_go_bottom_page()
    pricing.gocardlesscard_option.click()
    pricing.submit_gocardless.click()
    time.sleep(5)


@then('Checkout international address for "(.*)" express delivery pipeline')
def _(context, your_country):
    address = CheckoutAddressPage(context)
    address.first_name.send_keys("qatest")
    address.last_name.send_keys("qatest")
    address.password.send_keys("password1234")
    address.opt_out_phone.click()
    address.opt_out_text.click()
    address.address_next.click()
    address.add_address_for_country(your_country)
    address.opt_in_email.click()
    address.get_dates.click()
    address.next.click()


@when('Checkout with OpenBanking')
def _(context):
    payment = PaymentPage(context)
    payment.checkout_openbanking()


@when('Checkout with gocardless account number "(.*)" and bank card "(.*)"')
def _(context, account_, bank_code):
    payment = PaymentPage(context)
    time.sleep(5)
    payment.local_details.click()
    payment.account_number.send_keys(account_)
    payment.scroll_down_page()
    time.sleep(1)
    payment.bank_code.send_keys(bank_code)
    payment.submit_bank.click()
    payment.submit_order.click()


@then('Signup completed "(.*)" displays')
def _(context, thank_you):
    payment = PaymentPage(context)
    assert thank_you in payment.header.text


@then('Signup completed and "(.*)" display pipeline')
def _(context, my_dashboard):
    signup_complete = DashboardPage(context)
    signup_complete.continue_dashboard.click()


@when('Signup completed and "(.*)" display pipeline')
def _(context, my_dashboard):
    signup_complete = DashboardPage(context)
    signup_complete.continue_dashboard.click()


@then('Signup completed and france "(.*)" display pipeline')
def _(context, fr_dashboard):
    signup_complete = DashboardPage(context)
    signup_complete.fr_continue_dashboard.click()


@then('Signup completed and german "(.*)" display pipeline')
def _(context, de_dashboard):
    signup_complete = DashboardPage(context)
    signup_complete.de_continue_dashboard.click()


@then('Check each logged in page load for "(.*)" and "(.*)" and "(.*)" and "(.*)" and "(.*)" and "(.*)"')
def _(context, ftw, delivery, raf, account, update, name):
    dashboard = DashboardPage(context)
    navigation = NavigationPage(context)
    time.sleep(25)
    navigation.home_menu.click()
    dashboard.treatment_page.click()
    text = navigation.is_dashboard_ftw_loaded(ftw).text
    contains = text
    assert ftw in contains

    navigation.home_menu.click()
    dashboard.deliveries_page_select.click()
    time.sleep(7)
    text = navigation.is_dashboard_delivery_loaded(delivery).text
    contains = text
    assert delivery in contains
    time.sleep(15)
    navigation.home_menu.click()
    dashboard.raf_page_select.click()
    text = navigation.is_dashboard_raf_loaded(raf).text
    contains = text
    assert raf in contains

    navigation.home_menu.click()
    dashboard.account_page_select.click()

    text = navigation.is_dashboard_account_loaded(account).text
    contains = text
    assert account in contains

    navigation.home_menu.click()
    dashboard.profile_page_select.click()
    text = navigation.is_dashboard_profile_loaded(name).text
    contains = text
    assert name in contains

    navigation.home_menu.click()
    dashboard.feeding_plan_page_select.click()
    text = navigation.is_dashboard_feeding_plan_loaded(update).text
    contains = text
    assert update in contains


@then('Check shop page load for "(.*)" products')
def _(context, recommend):
    navigation = NavigationPage(context)
    dashboard = DashboardPage(context)
    navigation.home_menu.click()
    dashboard.shop_page_select.click()
    time.sleep(15)


@given('Logged in to "(.*)" customer account "(.*)" and store "(.*)" pipeline')
def _(context, country, seed_profile_type, store_id):
    dashboard_page = DashboardPage(context)
    home_page = HomePage(context)
    email = EmailPage(context)
    navigation = NavigationPage(context)
    cust_email = generate_email_customer_seed(seed_profile_type, store_id)

    home_page.goto("/")
    for cookie in context.browser.cookies_to_set:
        context.browser.add_cookie(cookie)

    home_page.country_select_login(country)
    email.country_for_login(country)
    # the following steps passing through password first then username
    # this is to overcome the android keyboard pop up preventing login
    # button click - do not change seq of steps
    email.email_password()
    email.email_login.send_keys(cust_email)

    navigation.login_button()

    # dashboard_page.dashboard_feed_survey_dismiss()
