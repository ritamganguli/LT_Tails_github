from behave import when, use_step_matcher
import time
from features.page_objects.dominant_breed_page import DominantPage

use_step_matcher("re")


@when('three crossbreed selection for dominant breed "(.*)" and "(.*)" and "(.*)"')
def _(context, firstbreed, secondbreed, thirdbreed):
    dominant = DominantPage(context)
    dominant_form = dominant.dominant_form
    first_breed = dominant.dominant_breed_first(firstbreed)
    time.sleep(5)
    second_breed = dominant.dominant_breed_first(secondbreed)
    time.sleep(5)
    third_breed = dominant.dominant_breed_first(thirdbreed)
    time.sleep(5)

    assert first_breed.text == firstbreed
    assert second_breed.text == secondbreed
    assert third_breed.text == thirdbreed
    time.sleep(5)
    dominant.dominant_breed_first(firstbreed).click()
    dominant_form.submit()


@when('Select first dominant breed go back "(.*)"')
def _(context, firstbreed_):
    dominant = DominantPage(context)
    time.sleep(7)
    dominant.dominant_breed_first(firstbreed_)
    time.sleep(7)
    dominant.first_dominant_breed.click()
    dominant.dominant_back.click()


@when("Select first dominant breed continue")
def _(context):
    dominant = DominantPage(context)
    dominant_form = dominant.dominant_form

    time.sleep(5)
    dominant.first_dominant_breed.click()
    dominant_form.submit()
