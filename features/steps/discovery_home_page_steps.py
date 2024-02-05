from behave import given, when, use_step_matcher
import time
from features.page_objects.home_page import HomePage

use_step_matcher("re")


@given('on homepage and "(.*)" country')
def _(context, country):
    home_page = HomePage(context)
    home_page.goto("/")
    time.sleep(5)

    for cookie in context.browser.cookies_to_set:
        context.browser.add_cookie(cookie)

    home_page.try_now.click()
    time.sleep(7)
    home_page.country.click()
    time.sleep(7)
    home_page.select_country(country)
    submit = home_page.country_submit
    assert submit.is_enabled()
    submit.click()
    time.sleep(10)


@given('On RAF page and "(.*)" country')
def _(context, _country):
    home_page = HomePage(context)
    home_page.goto("/friend/SOPHIEJ5/")
    hero = home_page.raf_hero

    if _country == "United Kingdom":
        assert "Jane has given you a free dry food trial" in hero.text

    time.sleep(5)


@when('Go into signup flow raf "(.*)"')
def _(context, country):
    home_page = HomePage(context)
    time.sleep(1)
    home_page.try_now_raf_page.click()
    home_page.select_country(country)
    submit = home_page.country_submit
    assert submit.is_enabled()
    submit.click()


@given('on homepage for prod box')
def _(context):
    home_page = HomePage(context)
    home_page.goto_prod()

    for cookie in context.browser.cookies_to_set_pb:
        context.browser.add_cookie(cookie)
    time.sleep(5)


@when('navigate into signup flow in "(.*)" country prod')
def _(context, country):
    home_page = HomePage(context)
    home_page.warning_close_cookie()
    time.sleep(7)
    home_page.try_now.click()
