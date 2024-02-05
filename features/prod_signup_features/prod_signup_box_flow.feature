@growth_regression
@prod_feature
@signup
Feature: Production Signup

    @prod_uk
   @prod_uk_puppy
   Scenario: prod001: puppy exclude lamb - UK prod signup
    Given on homepage for prod box
    When navigate into signup flow in "United Kingdom" country prod
    When Add "beagle" information age "0" years "2" months female not spayed purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working dog weight "6" just right weight
    And Health issues none and ingredients excluded lamb
    And Current diet select dry wet food and treats other food
    And Current food selected wet "Mini can (156g)"
    And Select flavour anything
    And Complete email page
    Then Dry page contain no "lamb" for puppy

   @prod_uk
   @prod_hypo
  Scenario: prod002 hypoallergenic - UK prod signup
    Given on homepage for prod box
    When navigate into signup flow in "United Kingdom" country prod
    And Add "dogonetest" information age "2" years "5" months male neutered purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no health issues with hypoallergenic UK
    And Current diet dry food
    And Current food select no brand
    And Select flavour anything
    And Complete email page for prod
    Then Dry and treats page contain no hypo ingredients in "United Kingdom"

   @prod_uk
   @prod_exclusions
  Scenario: prod003 excluded ingredients - UK prod signup
    Given on homepage for prod box
    When navigate into signup flow in "United Kingdom" country prod
    And Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health issues none and ingredients excluded wheat beef chicken soya fish dairy egg
    And Current diet dry food
    And Current food select no brand
    And Select flavour anything
    And Complete email page for prod
    Then Dry page contain no "Wheat" "Beef" "Chicken" "Soya" "Fish" "Dairy" "Egg"

  @prod_uk
  @prod_uk_remote
  Scenario: prod006 dry & wet food & treats isle postcode no express - UK prod signup
    Given on homepage for prod box
    When navigate into signup flow in "United Kingdom" country prod
    When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues UK
    And Current diet select dry and wet food
    And Current food no dry selected wet "Mini can (156g)"
    And Select flavour anything
    And Complete email page
    And select dry and wet Project Box in "United Kingdom"
    And Select no treats Project Box
    And Pricing continue with card
    Then Checkout with remote postcode "PH106LP"

  @prod_uk
  @prod_uk_express
  Scenario: prod005 dry & wet food & dental dailies express delivery - UK prod signup
    Given on homepage for prod box
    When navigate into signup flow in "United Kingdom" country prod
    When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues UK
    And Current diet select dry and wet food
    And Current food no dry selected wet "Mini can (156g)"
    And Select flavour anything
    And Complete email page
    And select dry and wet in United Kingdom while dry and wet in current diet
    And select dental dailies treats Project Box in "United Kingdom"
    And Pricing page with "Dental dailies"
    Then Checkout address postcode "TW92SS" express delivery
