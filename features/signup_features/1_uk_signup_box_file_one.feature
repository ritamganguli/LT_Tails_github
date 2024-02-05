@growth_regression
@uk_feature_no_checkout
@signup
Feature: UK Signup no checkout

  @uk_remote
  @nightly_chrome_one
  Scenario: 006 dry & wet food & treats isle postcode no express - UK signup
    Given on homepage and "United Kingdom" country
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

  @uk_resume_dominantbreed
  @nightly_iphone_two
   Scenario: 007 dominant breed - UK signup
    Given on homepage and "United Kingdom" country
    When Add "dogone" information age "2" years "5" months male neutered three crossbreed "Labrador Retriever" and "Cockapoo" and "Pomeranian"
    And Select first dominant breed go back "Pomeranian"
    And Add third breed "Beagle" and "Alapaha Blue Blood Bulldog" and "Pomeranian"
    And three crossbreed selection for dominant breed "Beagle" and "Alapaha Blue Blood Bulldog" and "Pomeranian"
    And Select gain weight motivation for dog food


  @uk_partial_crossbreed
  @nightly_chrome_two
  Scenario: 008 partial - UK signup
    Given on homepage and "United Kingdom" country
    When Add "dogone" information age "2" years "5" months male neutered two crossbreed "Beagle" and "Bulldog"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues UK
    And Current diet dry food
    And Current food select no brand
    And Select flavour anything
    And Navigate to Home logo
    Then can continue signup for uk "Dogone"

  @uk_health_all_unknown_breed
  @nightly_android_one
  Scenario: 009 health concerns all - UK signup
    Given on homepage and "United Kingdom" country
    When Add "dogone" information age "2" years "5" months male neutered unknown breed selected "Giant (over 40kg)" for "UK"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And health all issues Joints Skin and coat Digestion Pancreatitis exclusions none UK
    And Current diet dry food
    And Current food select no brand
    And Select flavour anything
    And Complete email page
    Then Dry page display all health issues in "United Kingdom"


  @uk_hypo
  @nightly_android_three
  Scenario: 010 hypoallergenic - UK signup
    Given on homepage and "United Kingdom" country
    When Add "dogonetest" information age "2" years "5" months male neutered purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no health issues with hypoallergenic UK
    And Current diet dry food
    And Current food select no brand
    And Select flavour anything
    And Complete email page
    Then Dry and treats page contain no hypo ingredients in "United Kingdom"


  @uk_exclusions
  @nightly_chrome_two
  Scenario: 011 excluded ingredients - UK signup
    Given on homepage and "United Kingdom" country
    When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health issues none and ingredients excluded wheat beef chicken soya fish dairy egg
    And Current diet dry food
    And Current food select no brand
    And Select flavour anything
    And Complete email page
    Then Dry page contain no "Wheat" "Beef" "Chicken" "Soya" "Fish" "Dairy" "Egg"

  @uk_excl_soya
  @nightly_android_two
  Scenario: 012 soya excluded ingredients - UK signup
    Given on homepage and "United Kingdom" country
    When Add "puppy dalm" information age "0" years "5" months female not spayed purebreed "Dalmatian"
    And Select gain weight motivation for dog food
    And Status no working dog weight "34" just right weight and activity
    And Health issues skin and coat and ingredients excluded soya
    And Current diet select dry wet food and treats other food
    And Current food selected wet "Mini can (156g)"
    And Select flavour anything
    And Complete email page
    And Dry food page display tailored to needs "Healthy skin & coat"
    Then Dry page contain no "Soya" for dalmation


  @uk_excl_lamb
  @nightly_chrome_two
  Scenario: 013 Lamb excluded ingredients - UK signup
    Given on homepage and "United Kingdom" country
    When Add "lamb spaniel" information age "0" years "2" months female not spayed purebreed "English Springer Spaniel"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15" just right weight
    And Health issues none and ingredients excluded lamb
    And Current diet select dry wet food and treats other food
    And Current food selected wet "Mini can (156g)"
    And Select flavour anything
    And Complete email page
    Then Dry page contain no "lamb" for puppy


  @uk_puppy
  @nightly_chrome_two
  Scenario: 014 puppy - UK signup
    Given on homepage and "United Kingdom" country
    When Add "beagle" information age "0" years "2" months female not spayed purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working puppy weight "6"
    And Health issues "English" selected lamb and wheat
    And Current diet select dry and wet food
    And Current food no dry selected wet "Mini can (156g)"
    And Select flavour anything
    And Complete email page
    Then Dry page contain no ingredients "wheat" for puppy


  @uk_pregnant
  @nightly_android_three
  Scenario: 015 pregnant/nursing - UK signup
    Given on homepage and "United Kingdom" country
    When one dog female not spayed "pregnant"
    And is pregnant
    Then alert display for no unique recipes for pregnant dogs

  @uk_specbreed
  @nightly_android_one
  Scenario: 016 special breed - UK signup
    Given on homepage and "United Kingdom" country
    When Add "dogone" information age "2" years "5" months male neutered special purebreed "Dalmation"
    Then alert for restricted protein

