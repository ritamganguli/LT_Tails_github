from behave import when, use_step_matcher
from features.page_objects.breed_page import BreedPage
from selenium.webdriver.common.keys import Keys
import time


use_step_matcher("re")


@when('Add third breed "(.*)" and "(.*)" and "(.*)"')
def _(context, firstbreed, secondbreed, thirdbreed):

    breed = BreedPage(context)
    breed_form = breed.breed_form
    time.sleep(10)
    breed.purebreed_input.click()
    breed.crossbreed_input.click()

    # First breed
    time.sleep(5)
    breed.crossbreed_search.clear()
    breed.crossbreed_search.send_keys(firstbreed)

    time.sleep(5)
    breed.crossbreed_search.send_keys(Keys.DOWN)

    # third breed
    breed.breed_search_third.clear()
    breed.breed_search_third.send_keys(thirdbreed)

    time.sleep(5)
    breed.breed_search_third.send_keys(Keys.DOWN)

    # Second breed
    time.sleep(5)
    breed.breed_search_second.clear()
    breed.breed_search_second.send_keys(secondbreed)
    time.sleep(5)
    breed.breed_search_second.send_keys(Keys.DOWN)

    breed_form.submit()
