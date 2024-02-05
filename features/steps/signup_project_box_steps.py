from behave import given, when, then, use_step_matcher
import time

from selenium.webdriver import ActionChains
from features.page_objects.navigation_page import NavigationPage
from features.page_objects.pricing_page import PricingPage
from features.page_objects.project_box_pages import ProjectBoxPages
from features.page_objects.home_page import HomePage

use_step_matcher("re")


@given('on homepage and "(.*)" country pb')
def _(context, country):
    home_page = HomePage(context)
    home_page.goto("/")

    for cookie in context.browser.cookies_to_set_pb:
        context.browser.add_cookie(cookie)

    time.sleep(7)
    home_page.try_now.click()
    home_page.country.click()
    home_page.select_country(country)
    submit = home_page.country_submit
    assert submit.is_enabled()
    submit.click()


@when('select dry food only Project Box')
def _(context):
    # core diet page
    box_page = ProjectBoxPages(context)
    time.sleep(7)
    box_page.add_to_box_button.click()
    time.sleep(10)


@when('select dry and wet Project Box in (.*)')
def _(context, country_for):
    # land on core diet page but go through to wet food link first
    box_page = ProjectBoxPages(context)
    time.sleep(15)
    box_page.see_wet_food.click()
    time.sleep(7)
    wet_page_header = box_page.wet_page_header
    # assert not "No trays available" in box_page.wet_food_card.text
    if country_for in ("United Kingdom", "Belgium", "Denmark", "Ireland", "Sweden"):
        assert "wet food selection" in wet_page_header.text
    if country_for in ("Germany", "Austria"):
        assert "Die Nassfutter-Auswahl" in wet_page_header.text

    # back to core diet page
    box_page.choose_this_selection_button.click()
    time.sleep(7)
    core_diet_header = box_page.core_diet_header
    if country_for in ("United Kingdom", "Belgium", "Denmark", "Ireland", "Sweden"):
        assert "unique feeding plan" in core_diet_header.text
    if country_for in ("Germany", "Austria"):
        assert "individuelle Ernährungsplan" in core_diet_header.text

    # core diet to treats via CTA
    box_page.add_to_box_button.click()
    time.sleep(15)
    essentials_page_header = box_page.essentials_page_header
    if country_for in ("United Kingdom", "Belgium", "Denmark", "Ireland", "Sweden"):
        assert "Handpicked" in essentials_page_header.text
    if country_for in ("Germany", "Austria"):
        assert "ausgewählt" in essentials_page_header.text
    if country_for == "Netherlands":
        assert "Handmatig geselecteerd" in essentials_page_header.text


@when('Select no treats Project Box')
def _(context):
    essentials_page = ProjectBoxPages(context)
    time.sleep(15)
    assert "None available" not in essentials_page.essentials_card.text
    assert "Oops" not in essentials_page.essentials_card.text
    assert "Apologies" not in essentials_page.essentials_card.text

    essentials_page.scroll_to_bottom_of_page()
    time.sleep(5)
    essentials_page.go_to_box_button.click()
    time.sleep(10)


@when('select dental dailies treats Project Box in "(.*)"')
def _(context, country_for):
    essentials_page = ProjectBoxPages(context)
    actions = ActionChains(essentials_page.browser)
    time.sleep(5)
    if country_for == "United Kingdom":
        dental_add_uk = essentials_page.dental_dailies_add_gb
        actions.move_to_element(dental_add_uk).click(dental_add_uk).perform()
    elif country_for == "France":
        dental_add_fr = essentials_page.dental_dailies_add_fr
        actions.move_to_element(dental_add_fr).click(dental_add_fr).perform()
    elif country_for in ("Germany", "Austria"):
        dental_add_de = essentials_page.dental_dailies_add_de
        actions.move_to_element(dental_add_de).click(dental_add_de).perform()
    else:
        dental_add_roe = essentials_page.dental_dailies_add_roe
        actions.move_to_element(dental_add_roe).click(dental_add_roe).perform()
    time.sleep(2)
    essentials_page.go_to_box_button.click()
    time.sleep(10)


@then('Dry page display all health issues in "(.*)"')
def _(context, country_for):
    box_page = ProjectBoxPages(context)
    time.sleep(7)
    health = box_page.claims
    if country_for in ("Germany", "Austria"):
        assert "Gesunde Haut & gesundes Fell" in health.text
        assert "Mobilität & Gelenkpflege" in health.text
        assert "Gesunde Verdauung" in health.text
    elif country_for == "Netherlands":
        assert "Gezonde huid & vacht" in health.text
        assert "Mobiliteit & gewrichtsverzorging" in health.text
        assert "Gezonde spijsvertering" in health.text
    elif country_for == "France":
        assert "Peau et pelage sains" in health.text
        assert "Mobilité et soins articulaires" in health.text
        assert "Bonne Digestion" in health.text
    else:
        assert "Healthy skin & coat" in health.text
        assert "Mobility & joint care" in health.text
        assert "Healthy digestion" in health.text


@then('Dry and treats page contain no hypo ingredients in "(.*)"')
def _(context, country_for):
    box_page = ProjectBoxPages(context)
    time.sleep(15)
    if country_for == "France":
        box_page.fr_dry_ingredients.click()
    elif country_for in ("Germany", "Austria"):
        box_page.de_dry_ingredients.click()
    elif country_for == "Netherlands":
        box_page.nl_dry_ingredients.click()
    else:
        box_page.dry_ingredient.click()
    ingredients = box_page.dry_ingredients
    time.sleep(7)
    if country_for in ("Germany", "Austria"):
        assert "Weizen" not in ingredients.text
        assert "Rindfleisch" not in ingredients.text
        assert "Soja" not in ingredients.text
        assert "Milchprodukte" not in ingredients.text
        assert "Ei" not in ingredients.text
    elif country_for == "Netherlands":
        assert "Zuivel" not in ingredients.text
        assert "Rundvlees" not in ingredients.text
        assert "Soja" not in ingredients.text
        assert "Tarwe" not in ingredients.text
        assert "Ei" not in ingredients.text
    elif country_for == "France":
        assert "Blé" not in ingredients.text
        assert "Bœuf" not in ingredients.text
        assert "Soja" not in ingredients.text
        assert "Produits laitiers" not in ingredients.text
        assert "Œuf" not in ingredients.text
    else:
        assert "Wheat" not in ingredients.text
        assert "Beef" not in ingredients.text
        assert "Soya" not in ingredients.text
        assert "Dairy" not in ingredients.text
        assert "Egg" not in ingredients.text


@then('Dry page contain no "(.*)" "(.*)" "(.*)" "(.*)" "(.*)" "(.*)" "(.*)"')
def _(context, wheat, beef, chicken, soya, fish, dairy, egg):
    box_page = ProjectBoxPages(context)
    box_page.dry_ingredient.click()
    ingredients = box_page.dry_ingredients
    time.sleep(7)
    assert wheat not in ingredients.text
    assert beef not in ingredients.text
    assert soya not in ingredients.text
    assert dairy not in ingredients.text
    assert egg not in ingredients.text
    assert chicken not in ingredients.text
    assert fish not in ingredients.text


@then('Dry page contain no "(.*)" for dalmation')
def _(context, soya):
    box_page = ProjectBoxPages(context)
    box_page.dry_ingredient.click()
    ingredients = box_page.dry_ingredients
    time.sleep(7)
    assert soya not in ingredients.text


@then('Dry page contain no "(.*)" for puppy')
def _(context, lamb):
    box_page = ProjectBoxPages(context)
    time.sleep(15)
    box_page.dry_ingredient.click()
    ingredients = box_page.dry_ingredients
    time.sleep(7)
    assert lamb not in ingredients.text


@then('Dry page contain no ingredients "(.*)" for puppy')
def _(context, wheat):
    box_page = ProjectBoxPages(context)
    box_page.dry_ingredient.click()
    ingredients = box_page.dry_ingredients
    time.sleep(7)
    assert wheat not in ingredients.text


@then('Dry page "(.*)" contains no exclusions "(.*)" "(.*)" and no option for wet food or treats')
def _(context, country_for, wheat, lamb):
    box_page = ProjectBoxPages(context)
    if country_for == "France":
        box_page.fr_dry_ingredients.click()
    elif country_for in ("Germany", "Austria"):
        box_page.de_dry_ingredients.click()
    elif country_for == "Netherlands":
        box_page.nl_dry_ingredients.click()
    else:
        box_page.dry_ingredient.click()
    ingredients = box_page.dry_ingredients
    time.sleep(10)
    assert wheat not in ingredients.text
    assert lamb not in ingredients.text

    own_wet = box_page.dry_own_wet_message
    if country_for in ("Germany", "Austria"):
        assert "derzeitigen Nassfutter" in own_wet.text
    elif country_for == "Netherlands":
        assert "het huidige natvoer" in own_wet.text
    elif country_for == "France":
        assert "portions de pâtée que vous servez actuellement" in own_wet.text
    else:
        assert "current wet food" in own_wet.text

    box_page.add_to_box_button.click()

    time.sleep(5)
    price_page = PricingPage(context)
    assert price_page.submit_pricing.is_enabled()


@when('Add promo "(.*)"')
def _(context, promo):
    box_page = ProjectBoxPages(context)
    box_page.add_promo.click()
    time.sleep(3)
    box_page.input_code.clear()
    box_page.input_code.send_keys(promo)
    box_page.apply_promo.click()


@when('select dry food only wet current diet pipeline in "(.*)"')
def _(context, country_for):
    box_page = ProjectBoxPages(context)
    time.sleep(7)
    core_diet_header = box_page.core_diet_header
    if country_for == "United Kingdom":
        assert "unique feeding plan" in core_diet_header.text
    if country_for == "Germany":
        assert "individuelle Ernährungsplan" in core_diet_header.text
    box_page.remove_wet_food.click()

    box_page.scroll_to_bottom_of_page()
    time.sleep(10)
    box_page.add_to_box_button.click()
    time.sleep(7)

    essentials_page_header = box_page.essentials_page_header
    if country_for == "United Kingdom":
        assert "Handpicked" in essentials_page_header.text
    if country_for == "Germany":
        assert "ausgewählt" in essentials_page_header.text


@when('select dry food only order while dry food only is in current diet in "(.*)"')
def _(context, country_for):
    box_page = ProjectBoxPages(context)
    time.sleep(7)
    core_diet_header = box_page.core_diet_header
    wet_upsell = box_page.wet_food_upsell_widget
    if country_for in ("United Kingdom", "Belgium", "Denmark", "Ireland", "Sweden"):
        assert "unique feeding plan" in core_diet_header.text
        assert "Why not add..." in wet_upsell.text
    if country_for in ("Germany", "Austria"):
        assert "individuelle Ernährungsplan" in core_diet_header.text
        assert "Wie wäre es mit..." in wet_upsell.text
    if country_for == "France":
        assert "programme alimentaire sur mesure" in core_diet_header.text
        assert "Et si vous ajoutiez…" in wet_upsell.text
    box_page.add_to_box_button.click()


@when("select dry and wet Project Box FR")
def _(context):
    box_page = ProjectBoxPages(context)
    time.sleep(27)

    # wet page via link
    box_page.see_wet_food_fr.click()
    time.sleep(15)
    wet_page_header = box_page.wet_page_header
    assert "barquettes" in wet_page_header.text

    assert "No trays available" not in box_page.wet_food_card.text
    assert "Aucun plateau disponible" not in box_page.wet_food_card.text
    box_page.choose_this_selection_button.click()

    # core diet page
    core_diet_header = box_page.core_diet_header
    assert "programme alimentaire" in core_diet_header.text
    box_page.add_to_box_button.click()

    # treats page - not working for now need to fix
    time.sleep(15)
    essentials_page_header = box_page.essentials_page_header
    assert "Choisi" in essentials_page_header.text


@when("Select dry food only")
def _(context):
    box_page = ProjectBoxPages(context)
    time.sleep(7)
    box_page.add_to_box_button.click()
    time.sleep(10)


@when("select dry food only Project Box and add another dog")
def _(context):
    # core diet page
    box_page = ProjectBoxPages(context)
    time.sleep(7)
    box_page.add_to_box_button.click()
    time.sleep(7)

    essentials_page = ProjectBoxPages(context)
    essentials_page.go_to_box_button.click()
    # time.sleep(15)

    pricing = PricingPage(context)
    pricing.another_dog.click()
    # time.sleep(10)
    navigate = NavigationPage(context)
    navigate.pets_another_dog.click()


@when('select dry and wet in (.*) while dry only current diet')
def _(context, country_for):
    # land on core diet page but go through to add wet food first
    box_page = ProjectBoxPages(context)
    time.sleep(7)
    context.browser.execute_script("window.scrollBy(0,600);")
    box_page.see_wet_food_upsell.click()
    nav = NavigationPage(context)
    time.sleep(5)
    wet_page_header = box_page.wet_page_header
    if country_for == "United Kingdom":
        assert "wet food selection" in wet_page_header.text
    if country_for in ("Germany", "Austria"):
        assert "Die Nassfutter-Auswahl" in wet_page_header.text
    if country_for == "France":
        assert "de barquettes" in wet_page_header.text
    time.sleep(5)
    nav.check_height_page_go_bottom_page()
    # back to core diet page
    box_page.choose_this_selection_button.click()

    time.sleep(5)
    box_page.add_to_box_button.click()
    time.sleep(10)
    core_diet_header = box_page.core_diet_header
    if country_for == "United Kingdom":
        assert "unique feeding plan" in core_diet_header.text
    if country_for in ("Germany", "Austria"):
        assert "individuelle Ernährungsplan" in core_diet_header.text
    if country_for == "France":
        assert "programme alimentaire" in core_diet_header.text

    # core diet to treats via CTA
    box_page.add_to_box_button.click()
    # time.sleep(10)
    essentials_page_header = box_page.essentials_page_header
    if country_for == "United Kingdom":
        assert "Handpicked" in essentials_page_header.text
    if country_for in ("Germany", "Austria"):
        assert "ausgewählt" in essentials_page_header.text
    if country_for == "France":
        assert "Choisi" in essentials_page_header.text


@when('select dry and wet in (.*) while dry and wet in current diet')
def _(context, country_for):
    # land on core diet page but go through to add wet food first
    box_page = ProjectBoxPages(context)

    time.sleep(7)
    box_page.see_wet_food.click()
    time.sleep(15)
    wet_page_header = box_page.wet_page_header
    if country_for == "United Kingdom":
        assert "wet food selection" in wet_page_header.text
    if country_for in ("Germany", "Austria"):
        assert "Die Nassfutter-Auswahl" in wet_page_header.text
    if country_for == "France":
        assert "de barquettes" in wet_page_header.text

    # back to core diet page
    box_page.choose_this_selection_button.click()
    time.sleep(5)
    # core_diet_header = box_page.core_diet_header
    # if country_for == "United Kingdom":
    #     assert "unique feeding plan" in core_diet_header.text
    # if country_for in ("Germany", "Austria"):
    #     assert "individuelle Ernährungsplan" in core_diet_header.text
    # if country_for == "France":
    #     assert "alimentation" in core_diet_header.text

    # core diet to treats via CTA
    box_page.add_to_box_button.click()
    time.sleep(15)
    essentials_page_header = box_page.essentials_page_header
    if country_for == "United Kingdom":
        assert "Handpicked" in essentials_page_header.text
    if country_for in ("Germany", "Austria"):
        assert "ausgewählt" in essentials_page_header.text
    if country_for == "France":
        assert "Choisi" in essentials_page_header.text


@then('Dry page "(.*)" contain no excluded ingredients')
def _(context, country_for):
    box_page = ProjectBoxPages(context)
    if country_for == "France":
        box_page.fr_dry_ingredients.click()
    elif country_for in ("Germany", "Austria"):
        box_page.de_dry_ingredients.click()
    elif country_for == "Netherlands":
        box_page.nl_dry_ingredients.click()
    else:
        box_page.dry_ingredient.click()
    box_page.dry_ingredients.click()
    ingredients = box_page.dry_ingredients
    time.sleep(7)
    if country_for in ("Germany", "Austria"):
        assert "Weizen" not in ingredients.text
        assert "Rindfleisch" not in ingredients.text
        assert "Soja" not in ingredients.text
        assert "Fisch" not in ingredients.text
        assert "Milchprodukte" not in ingredients.text
        assert "Ei" not in ingredients.text
    elif country_for == "Netherlands":
        assert "Zuivel" not in ingredients.text
        assert "Rundvlees" not in ingredients.text
        assert "Soja" not in ingredients.text
        assert "Tarwe" not in ingredients.text
        assert "Ei" not in ingredients.text
        assert "Kip" not in ingredients.text
        assert "Vis" not in ingredients.text
    elif country_for == "France":
        assert "Blé" not in ingredients.text
        assert "Bœuf" not in ingredients.text
        assert "Poisson" not in ingredients.text
        assert "Poulet" not in ingredients.text
        assert "Soja" not in ingredients.text
        assert "Produits laitiers" not in ingredients.text
        assert "Œuf" not in ingredients.text
    else:
        assert "Wheat" not in ingredients.text
        assert "Beef" not in ingredients.text
        assert "Soya" not in ingredients.text
        assert "Dairy" not in ingredients.text
        assert "Egg" not in ingredients.text
        assert "Chicken" not in ingredients.text
        assert "Fish" not in ingredients.text


@then('Updating wet food flavours/textures displays correct wet food selection in "(.*)"')
def _(context, country_for):
    box_page = ProjectBoxPages(context)

    # Update flavour/texture selection
    box_page.see_wet_food.click()
    time.sleep(15)
    box_page.change_wet_food_flavours_textures.click()
    time.sleep(15)
    # actions.move_to_element(box_page.chicken_flavour_radio).click(box_page.chicken_flavour_radio).perform()
    box_page.chicken_flavour_radio.click()
    box_page.lamb_flavour_radio.click()
    box_page.pate_texture_radio.click()
    box_page.confirm_new_wet_food_selection.click()
    time.sleep(15)

    # Confirm new wet food selection is correct
    if country_for == "Germany":
        assert "Huhn" not in box_page.wet_food_selection_cards.text
        assert "Lamm" not in box_page.wet_food_selection_cards.text
        assert "Pastete" not in box_page.wet_food_selection_cards.text
    elif country_for == "France":
        assert "Poulet" not in box_page.wet_food_selection_cards.text
        assert "Agneau" not in box_page.wet_food_selection_cards.text
        assert "Pâté" not in box_page.wet_food_selection_cards.text
    else:
        assert "Chicken" not in box_page.wet_food_selection_cards.text
        assert "Lamb" not in box_page.wet_food_selection_cards.text
        assert "Pâté" not in box_page.wet_food_selection_cards.text

    box_page.close_notification.click()
    box_page.scroll_up_page()
    time.sleep(10)
    box_page.back_button.click()
    assert box_page.beef_flavour_icon.is_enabled()
    box_page.no_lamb_flavour_icon()
    box_page.no_chicken_flavour_icon()
    time.sleep(5)

#
# @then('Wet food flavours/textures accordion displays correct selection in "(.*)"')
# def _(context, country_for):
#     box_page = ProjectBoxPages(context)


@then('Wet food flavours/textures accordion displays correct selection in "(.*)"')
def _(context, country_for):
    box_page = ProjectBoxPages(context)

    # Update flavour/texture selection
    box_page.see_wet_food.click()
    time.sleep(2)
    box_page.change_wet_food_flavours_textures.click()
    box_page.no_lamb_flavour_icon()


@when('Add "(.*)" Project Box and claim "(.*)"')
def _(context, _product, _claim):
    essentials_page = ProjectBoxPages(context)
    time.sleep(5)
    essentials_page.scroll_down_page()

    # only poo  bags have claims in FR and DE
    # for the test to work, use the translated product name in the feature file parameters

    if _product.lower() == "superfood lamb bites":
        essentials_page.superfood_add.click()
        _product = "super-lamb-bites"
    if _product.lower() == "good dog treats":
        essentials_page.good_dog_add.click()
        _product = "good-dog-treats"
    if _product.lower() == "dental dailies":
        essentials_page.dental_dailies_add_button.click()
        # needs editing if large or small
        _product = "medium-dental-dailies"
    if _product.lower() == "poo bags":
        essentials_page.poo_bags_add.click()
        _product = "poo-bags-recycled"
    if _product.lower() == "chicken biscuits":
        essentials_page.chicken_biscuits_add.click()
        _product = "chicken-biscuits"
    if _product.lower() == "natural chew":
        essentials_page.natural_chew_add.click()
        _product = "natural-chews-pig-ears"
    if _product.lower() == "fresh chew":
        essentials_page.fresh_chew_medium_add.click()
        _product = "fresh-chews-medium"
    if _product.lower() == "leckerbissen":
        essentials_page.good_dog_add_de.click()
    if _product.lower() == "enten-Kekse":
        essentials_page.duck_biscuits_de.click()
    if _product.lower() == "bâtonnets dentaires":
        essentials_page.dental_dailies_add_fr.click()
    if _product.lower() == "les petites bouchées":
        essentials_page.good_dog_add_fr.click()
    if _product.lower() == "biscuits au saumon":
        essentials_page.salmon_biscuits_fr.click()
    if _product.lower() == "natürliche kausnacks - schweineohren":
        essentials_page.natural_chew_de_add.click()
        _product = "natuerliche-kausnacks-schweineohren"

    essentials_page.check_claim_essentials(_product, _claim)
    time.sleep(3)
    essentials_page.scroll_to_bottom_of_page()
    time.sleep(5)
    essentials_page.go_to_box_button.click()
    time.sleep(10)


@then('Confirm "(.*)" not shown')
def _(context, _product):
    essentials_page = ProjectBoxPages(context)

    if _product == "super food lamb":
        _product = "super-lamb-bites"
        essentials_page.product_not_shown(_product)
