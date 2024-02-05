from behave import when, then, use_step_matcher
import time
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from features.page_objects.navigation_page import NavigationPage
from features.page_objects.checkout_address_page import CheckoutAddressPage

use_step_matcher("re")


@when('Checkout address postcode "(.*)" future delivery date')
def _(context, pcodeuk):
    address = CheckoutAddressPage(context)
    nav = NavigationPage(context)
    time.sleep(5)
    address.first_name.send_keys("qatest")
    address.last_name.send_keys("qatest")
    address.password.send_keys("password1234")
    address.opt_out_phone.click()
    address.opt_out_text.click()
    address.scroll_down_page()
    time.sleep(5)
    address.next.click()
    time.sleep(5)

    address.search_postcode.send_keys(pcodeuk)
    nav.dismiss_keyboard()
    address.postcode_lookup.click()
    nav.dismiss_keyboard()
    time.sleep(15)
    context.browser.execute_script("window.scrollBy(0,300);")
    address.address_select_uk()
    address.opt_out_email.click()
    address.get_dates.click()
    time.sleep(3)
    address.future_delivery_date()
    address.scroll_down_page()
    time.sleep(3)
    address.next.click()


@then('Checkout address postcode "(.*)" express delivery')
def _(context, uk_pcode):
    address = CheckoutAddressPage(context)

    address.first_name.send_keys("qatest")
    address.last_name.send_keys("qatest")
    address.password.send_keys("password1234")
    address.opt_out_phone.click()
    address.opt_out_text.click()
    time.sleep(5)
    address.address_next.click()

    address.search_postcode.send_keys(uk_pcode)
    address.postcode_lookup.click()
    address.opt_in_email.click()
    time.sleep(15)
    address.address_select_uk()
    time.sleep(7)
    address.get_dates.click()
    time.sleep(5)
    address.next.click()


@then('Checkout with remote postcode "(.*)"')
def _(context, postc_remote):
    address = CheckoutAddressPage(context)
    nav = NavigationPage(context)
    address.first_name.send_keys("qatest")
    address.last_name.send_keys("qatest")
    address.password.send_keys("password1234")
    address.opt_out_phone.click()
    address.opt_out_text.click()
    time.sleep(2)
    address.address_next.click()

    address.search_postcode.send_keys(postc_remote)
    nav.dismiss_keyboard()
    # address.search_postcode_uk(postc_remote)
    address.postcode_lookup.click()
    address.opt_in_email.click()
    time.sleep(10)
    context.browser.execute_script("window.scrollBy(0,300);")
    address.remote_address_select()
    time.sleep(10)
    address.get_dates.click()
    address.next.click()
    time.sleep(10)


@when("Checkout address for France future delivery date")
def _(context):
    address = CheckoutAddressPage(context)
    address.first_name.send_keys("qatest")
    address.last_name.send_keys("qatest")
    address.password.send_keys("password1234")
    address.scroll_down_page()
    time.sleep(1)
    address.opt_out_phone.click()
    address.opt_out_text.click()
    time.sleep(5)
    address.address_next.click()

    address.address_france()
    address.opt_in_email.click()
    time.sleep(10)
    address.scroll_down_page()
    time.sleep(1)
    address.get_dates.click()
    time.sleep(1)
    time.sleep(10)
    address.future_delivery_date()
    address.next_fr.click()


@then("Checkout address for France express delivery")
def _(context):
    address = CheckoutAddressPage(context)
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


@when('Checkout international address for "(.*)" future delivery date')
def _(context, your_country):
    address = CheckoutAddressPage(context)
    address.first_name.send_keys("qatest")
    address.last_name.send_keys("qatest")
    address.password.send_keys("password1234")
    address.scroll_down_page()
    time.sleep(7)
    address.opt_out_phone.click()
    address.opt_out_text.click()
    time.sleep(5)
    address.address_next.click()
    address.add_address_for_country(your_country)
    address.opt_in_email.click()
    time.sleep(10)

    address.scroll_down_page()
    time.sleep(1)
    address.get_dates.click()

    time.sleep(10)
    address.future_delivery_date()
    time.sleep(7)
    address.next.click()


@then('Checkout international address for "(.*)" express delivery')
def _(context, your_country):
    address = CheckoutAddressPage(context)
    address.first_name.send_keys("qatest")
    address.last_name.send_keys("qatest")
    address.password.send_keys("password1234")
    address.scroll_down_page()
    time.sleep(1)
    address.opt_out_phone.click()
    address.opt_out_text.click()
    time.sleep(5)
    address.address_next.click()
    address.add_address_for_country(your_country)
    address.opt_in_email.click()
    time.sleep(5)
    address.scroll_down_page()
    time.sleep(5)
    if your_country == "Germany":
        address.get_dates_de.click()
    else:
        address.get_dates.click()
    actions = ActionChains(address.browser)
    actions.move_to_element(address.next).click(address.next).perform()


@when('Checkout international address for "(.*)" express delivery')
def _(context, your_country):
    address = CheckoutAddressPage(context)
    address.first_name.send_keys("qatest")
    address.last_name.send_keys("qatest")
    address.password.send_keys("password1234")
    address.scroll_down_page()
    time.sleep(1)
    address.opt_out_phone.click()
    address.opt_out_text.click()
    time.sleep(5)
    address.address_next.click()
    address.add_address_for_country(your_country)
    address.opt_in_email.click()
    time.sleep(5)
    address.get_dates.click()
    address.next.click()


@when('Checkout address postcode "(.*)" for France future delivery date')
def _(context, fr_postcode):
    address = CheckoutAddressPage(context)
    address.first_name.send_keys("qatest")
    address.last_name.send_keys("qatest")
    address.password.send_keys("password1234")
    time.sleep(5)
    address.address_next.click()
    time.sleep(5)
    address.scroll_to_bottom_of_page()
    address.fr_postcode.send_keys(fr_postcode)
    address.address_france()

    time.sleep(5)
    address.fr_get_dates.click()
    address.future_delivery_date()
    address.next.click()


@then('Checkout international address postcode "(.*)" for France express delivery')
def _(context, fr_postcode):
    address = CheckoutAddressPage(context)
    address.first_name.send_keys("qatest")
    address.last_name.send_keys("qatest")
    address.password.send_keys("password1234")
    time.sleep(5)
    address.address_next.click()
    address.address_france()
    time.sleep(5)
    address.scroll_to_bottom_of_page()
    address.fr_postcode.send_keys(fr_postcode)
    address.address_france()

    time.sleep(5)
    address.fr_get_dates.click()
    address.next.click()


@when("checkout securely")
def _(context):
    address = CheckoutAddressPage(context)
    time.sleep(15)
    address.checkout_securely.click()


@when('Checkout address postcode "(.*)" future delivery date redesign')
def _(context, pcodeuk):
    address = CheckoutAddressPage(context)
    time.sleep(7)
    address.first_name.send_keys("qatest")
    address.last_name.send_keys("qatest")
    address.password.send_keys("password1234")
    address.opt_out_phone.click()
    address.opt_out_text.click()
    address.scroll_down_page()
    time.sleep(5)
    address.next_page()
    time.sleep(5)

    address.search_postcode_uk(pcodeuk)
    time.sleep(5)
    address.postcode_lookup_redesign.click()
    time.sleep(10)
    address.address_select_uk()
    address.opt_out_email.click()
    time.sleep(10)
    address.get_dates.click()
    time.sleep(7)

    address.next_page()
