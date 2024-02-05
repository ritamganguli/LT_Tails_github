@growth_regression
@france_no_checkout
@signup
Feature: France Signup


  @france_resume
  Scenario: 106 incomplete and resume signup - FR signup
   Given on homepage and "France" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet dry food
   And Current food select no brand
   And Select flavour anything
   Then complete signup with email "France"

  @france_partial
  Scenario: 107 partial - FR signup
   Given on homepage and "France" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet dry food
   And Current food select no brand
   And Select flavour anything
   And Navigate to Home logo
   Then can Continue signup "Dogone"

  @france_health
  @nightly_iphone_two
   Scenario: 108 health concerns all - FR signup
   Given on homepage and "France" country
   When Add "iphone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And health all issues Joints Skin and coat Digestion Pancreatitis in "France"
   And Current diet dry food
   And Current food select no brand
   And Select flavour anything
   And Complete email page
   Then Dry page display all health issues in "France"

  @france_hypo
  @nightly_iphone_two
  @nightly_android_one
  Scenario: 109 hypoallergenic - FR signup
     Given on homepage and "France" country
     When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
     And Select gain weight motivation for dog food
     And Status no working dog weight "15"
     And Health Ingredients all health issues with hypoallergenic
     And Current diet dry food
     And Current food select no brand
     And Select flavour anything
     And Complete email page
    Then Dry and treats page contain no hypo ingredients in "France"


  @france_exclusions
  @nightly_iphone_three
  Scenario:110 excluded ingredients - FR signup
   Given on homepage and "France" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health issues none and ingredients excluded wheat beef chicken soya fish dairy egg
   And Current diet dry food
   And Current food select no brand
   And Select flavour anything
   And Complete email page for petname "fr_110_exclude_ingr"
   Then Dry page "France" contain no excluded ingredients

  @france_puppy
  @nightly_chrome_one
  Scenario: 111 puppy - FR signup
   Given on homepage and "France" country
   When Add "frdog" information age "0" years "2" months female not spayed purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working puppy weight "6"
   And Health issues "France" selected lamb and wheat
   And Current diet select dry and wet food
   And Current food no dry selected wet "Mini conserve (156g)"
   And Select flavour anything
   And Complete email page
   Then Dry page "France" contains no exclusions "Blé" "Agneau" and no option for wet food or treats


  @france_pregnant
  @nightly_iphone_two
  Scenario: 112 pregnant/nursing - FR signup
    Given on homepage and "France" country
    When one dog female not spayed "pregnant"
    And is pregnant
    Then france alert display for no unique recipes for pregnant dogs

  @france_specbreed
  @nightly_iphone_three
  Scenario: 113 special breed - FR signup
    Given on homepage and "France" country
    When Add "dogone" information age "2" years "5" months male neutered special purebreed "Dalmation"
    Then france alert for restricted protein

