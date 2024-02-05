from behave import when, then, use_step_matcher
import time
from features.page_objects.mydog_page import MydogPage
from features.page_objects.breed_page import BreedPage
from features.page_objects.unknown_breed_page import UnknownBreedPage
from selenium.webdriver.common.keys import Keys
from features.page_objects.navigation_page import NavigationPage

use_step_matcher("re")


@when(
    'Add "(.*)" information age "(.*)" years "(.*)" months male neutered purebreed'
    ' "(.*)"'
)
def _(context, dogn, yr, mth, pure_breed_):
    dog = MydogPage(context)
    dog.name_input.send_keys(dogn)
    nav = NavigationPage(context)
    nav.dismiss_keyboard()

    time.sleep(3)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   dog.male_input)

    dog.male_input.click()
    dog.neutered_yes.click()
    dog.years_input.send_keys(yr)
    nav.dismiss_keyboard()
    dog.months_input.send_keys(mth)
    nav.dismiss_keyboard()

    dog_form = dog.dog_form
    dog_form.submit()

    breed = BreedPage(context)
    breed_form = breed.breed_form
    breed.purebreed_input.click()
    time.sleep(2)
    breed.crossbreed_input.click()
    breed.purebreed_input.click()
    time.sleep(7)
    breed.breed_search.send_keys(pure_breed_)

    time.sleep(5)
    breed.breed_search.send_keys(Keys.DOWN)

    breed_form.submit()


@when('Add "(.*)" information age "(.*)" years "(.*)" months male neutered two crossbreed "(.*)" and "(.*)"')
def _(context, dogn, yr, mth, firstbreed, secondbreed):
    dog = MydogPage(context)
    time.sleep(5)
    dog.name_input.send_keys(dogn)

    time.sleep(3)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   dog.male_input)

    dog.male_input.click()

    dog.neutered_yes.click()
    dog.years_input.send_keys(yr)
    dog.months_input.send_keys(mth)

    dog_form = dog.dog_form
    dog_form.submit()

    breed = BreedPage(context)
    breed_form = breed.breed_form

    time.sleep(5)
    breed.crossbreed_input.click()

    # First breed
    time.sleep(7)
    breed.crossbreed_search.send_keys(firstbreed)
    time.sleep(5)
    breed.crossbreed_search.send_keys(Keys.DOWN)

    # Second breed
    time.sleep(5)
    breed.breed_search_second.send_keys(secondbreed)

    time.sleep(5)
    breed.breed_search_second.send_keys(Keys.DOWN)

    breed_form.submit()


@when(
    'Add "(.*)" information age "(.*)" years "(.*)" months male neutered three crossbreed "(.*)" and "(.*)" and "(.*)"')
def _(context, dogn, yr, mth, firstbreed, secondbreed, thirdbreed):
    dog = MydogPage(context)
    time.sleep(5)
    dog.name_input.send_keys(dogn)

    time.sleep(3)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   dog.male_input)

    dog.male_input.click()
    dog.neutered_yes.click()
    dog.years_input.send_keys(yr)
    dog.months_input.send_keys(mth)

    dog_form = dog.dog_form
    dog_form.submit()

    breed = BreedPage(context)
    breed_form = breed.breed_form

    time.sleep(2)
    breed.crossbreed_input.click()

    # First breed
    time.sleep(5)
    breed.crossbreed_search.send_keys(firstbreed)
    time.sleep(5)
    breed.crossbreed_search.send_keys(Keys.DOWN)

    # Second breed
    time.sleep(2)
    breed.breed_search_second.send_keys(secondbreed)
    time.sleep(5)
    breed.breed_search_second.send_keys(Keys.DOWN)

    # third breed
    time.sleep(5)
    breed.breed_search_third.send_keys(thirdbreed)
    time.sleep(5)
    breed.breed_search_third.send_keys(Keys.DOWN)
    breed_form.submit()


@when(
    'Add "(.*)" information age "(.*)" years "(.*)" months male neutered unknownbreed'
    ' "(.*)"'
)
def _(context, dogn, yr, mth, unknown_breed_):
    dog = MydogPage(context)
    dog.name_input.send_keys(dogn)
    nav = NavigationPage(context)
    nav.dismiss_keyboard()

    time.sleep(3)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   dog.male_input)
    context.browser.execute_script("window.scrollBy(0,200);")
    dog.male_input.click()
    dog.neutered_yes.click()
    dog.years_input.send_keys(yr)
    nav.dismiss_keyboard()
    dog.months_input.send_keys(mth)
    nav.dismiss_keyboard()

    context.browser.execute_script("window.scrollBy(0,300);")
    dog_form = dog.dog_form
    dog_form.submit()

    breed = BreedPage(context)
    breed_form = breed.breed_form

    breed.unknown_breed.click()
    breed_form.submit()
    time.sleep(10)

    unknown = UnknownBreedPage(context)
    unknown_breed_form = unknown.unknown_breed_form
    unknown.select_unknown(unknown_breed_)

    unknown_breed_form.submit()


@when('Add "(.*)" information age "(.*)" years "(.*)" months male neutered unknown breed selected "(.*)" for "(.*)"')
def _(context, dogn, yr, mth, unknown_breed_, country_):
    dog = MydogPage(context)
    time.sleep(5)
    dog.name_input.send_keys(dogn)

    time.sleep(3)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   dog.male_input)

    dog.male_input.click()
    dog.neutered_yes.click()
    dog.years_input.send_keys(yr)
    dog.months_input.send_keys(mth)

    dog_form = dog.dog_form
    dog_form.submit()

    breed = BreedPage(context)
    breed_form = breed.breed_form

    breed.unknown_breed.click()
    breed_form.submit()
    time.sleep(2)

    unknown = UnknownBreedPage(context)
    unknown_breed_form = unknown.unknown_breed_form
    time.sleep(7)
    if country_ == "UK":
        unknown_select_ = unknown.unknown_breed_giant_uk
        unknown.select_unknown(unknown_breed_)
        assert unknown_breed_ == unknown_select_.text
    if country_ == "NL":
        unknown_select = unknown.unknown_breed_giant_nl
        unknown.select_unknown(unknown_breed_)
        assert unknown_breed_ == unknown_select.text
    if country_ == "AT":
        unknown_select = unknown.unknown_breed_giant_at
        unknown.select_unknown(unknown_breed_)
        assert unknown_breed_ == unknown_select.text
    time.sleep(5)
    unknown_breed_form.submit()


@when('Add "(.*)" information age "(.*)" years neutered purebreed "(.*)"')
def _(context, dogn, yr, pure_breed_):
    dog = MydogPage(context)
    time.sleep(5)
    dog.name_input.send_keys(dogn)

    time.sleep(3)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   dog.male_input)

    dog.male_input.click()
    dog.neutered_yes.click()

    dog.years_input.send_keys(yr)

    dog_form = dog.dog_form
    dog_form.submit()

    breed = BreedPage(context)
    breed_form = breed.breed_form
    breed.purebreed_input.click()
    time.sleep(2)
    breed.crossbreed_input.click()
    breed.purebreed_input.click()
    time.sleep(7)
    breed.breed_search.send_keys(pure_breed_)
    time.sleep(5)
    breed.breed_search.send_keys(Keys.DOWN)
    breed_form.submit()


@when('Add "(.*)" information age "(.*)" years "(.*)" months female not spayed purebreed'
      ' "(.*)"')
def _(context, dogn, yr, mth, pure_breed_):
    dog = MydogPage(context)
    # time.sleep(5)
    dog.name_input.send_keys(dogn)

    time.sleep(7)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   dog.male_input)

    dog.male_input.click()

    time.sleep(2)

    dog.female_input.click()
    time.sleep(3)
    dog.neutered_no.click()
    dog.years_input.send_keys(yr)
    dog.months_input.send_keys(mth)

    dog_form = dog.dog_form
    dog_form.submit()

    pregnant = MydogPage(context)

    pregnant.pregnant_no.click()
    pregnant.pregnant_form.submit()

    puppy = MydogPage(context)
    puppy_birthday = puppy.puppy_form
    time.sleep(5)

    puppy.age_puppy_set(mth)
    puppy_birthday.submit()

    breed = BreedPage(context)
    breed_form = breed.breed_form
    breed.purebreed_input.click()
    time.sleep(2)
    breed.purebreed_input.click()
    time.sleep(7)
    breed.breed_search.send_keys(pure_breed_)
    time.sleep(5)
    breed.breed_search.send_keys(Keys.DOWN)
    breed_form.submit()


@then("france alert display for no unique recipes for pregnant dogs")
def _(context):
    pregnant = MydogPage(context)
    pregnant_form = pregnant.pregnant_form
    recipe = pregnant.france_no_recipe
    assert "Nous n’avons pas encore mis au point de recettes pour la grossesse" in recipe.text
    pregnant_form.submit()


@then("netherlands alert display for no unique recipes for pregnant dogs")
def _(context):
    pregnant = MydogPage(context)
    pregnant_form = pregnant.pregnant_form
    recipe = pregnant.netherlands_no_recipe
    assert "We maken op dit moment geen unieke recepten voor drachtige honden" in recipe.text
    pregnant_form.submit()


@then("german alert display for no unique recipes for pregnant dogs")
def _(context):
    pregnant = MydogPage(context)
    pregnant_form = pregnant.pregnant_form
    recipe = pregnant.german_no_recipe
    assert "Im Moment stellen" in recipe.text
    pregnant_form.submit()


@then("alert display for no unique recipes for pregnant dogs")
def _(context):
    pregnant = MydogPage(context)
    pregnant_form = pregnant.pregnant_form
    recipe = pregnant.no_recipe
    assert "At the moment" in recipe.text
    pregnant_form.submit()


@then("france alert for restricted protein")
def _(context):
    dog = MydogPage(context)
    restricted_ = dog.france_no_recipe_dalmation
    assert ("nous limitons les protéines" in restricted_.text)


@then("netherlands alert for restricted protein")
def _(context):
    dog = MydogPage(context)
    restricted_ = dog.netherlands_no_recipe_dalmation
    assert "Omdat Dalmatiërs vatbaar kunnen zijn voor uraatstenen" in restricted_.text


@then("german alert for restricted protein")
def _(context):
    dog = MydogPage(context)
    restricted_ = dog.german_no_recipe_dalmation
    assert "Wir reduzieren beim Futter für Dalmatiner den" in restricted_.text


@then('alert for restricted protein')
def _(context):
    dog = MydogPage(context)
    restrict = dog.no_recipe_dalmation
    assert (
            "We restrict protein and high purine ingredients for Dalmatians"
            in restrict.text
    )
    time.sleep(4)


@when('one dog female not spayed "(.*)"')
def _(context, femaledog):
    dog = MydogPage(context)
    dog.name_input.send_keys(femaledog)

    time.sleep(7)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   dog.male_input)

    dog.male_input.click()

    time.sleep(2)

    dog.female_input.click()
    time.sleep(3)
    dog.neutered_no.click()
    dog.years_input.send_keys("5")

    dog_form = dog.dog_form
    dog_form.submit()


@when("is pregnant")
def _(context):
    time.sleep(4)
    pregnant = MydogPage(context)
    pregnant.pregnant_yes.click()


@when(
    'Add "(.*)" information age "(.*)" years "(.*)" months male neutered special purebreed "(.*)"'
)
def _(context, name_dalmation, yr, mth, dalmation):
    dog = MydogPage(context)
    dog.name_input.send_keys(name_dalmation)

    time.sleep(7)
    # this scrolltoview selection is to  scroll it at the top and then by a 1/4th of the height of the view that the
    # zendesk widget doesn't intercept the click into update condition
    context.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -window.innerHeight / 4);",
                                   dog.male_input)

    dog.male_input.click()
    time.sleep(10)
    dog.neutered_yes.click()
    dog.years_input.send_keys(yr)
    dog.months_input.send_keys(mth)

    dog_form = dog.dog_form
    dog_form.submit()

    breed = BreedPage(context)
    breed.purebreed_input.click()
    breed.crossbreed_input.click()
    breed.purebreed_input.click()
    breed.breed_search.send_keys(dalmation)

    time.sleep(5)
    breed.breed_search.send_keys(Keys.DOWN)


@then('"(.*)" is displayed on the breed page')
def _(context, _alert):
    dog = MydogPage(context)
    message = dog.no_recipe_dalmation

    assert _alert in message.text


@then('Offer text is "(.*)"')
def _(context, promo_tongue):
    dog = MydogPage(context)
    time.sleep(3)
    trial = dog.promo_text

    assert promo_tongue in trial.text


@then('Confirm "(.*)" displays on the my-dog signup page')
def _(context, header):
    assert MydogPage(context).my_dog_header.text == header
