@growth_regression
@belgium_no_checkout
Feature: Belgium Signup box flow v2

  @belgium_resume
  @roe
  Scenario: 706 incomplete and resume signup - BE signup
   Given on homepage and "Belgium" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet dry food international
   And Select flavour anything
   Then complete signup with email "English"

  @belgium_partial
  @roe
  Scenario: 707 partial - BE signup
   Given on homepage and "Belgium" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet dry food international
   And Select flavour anything
   And Navigate to Home logo
   Then can Continue signup "Dogone"

  @belgium_health
  @roe
  @nightly_chrome_four
  Scenario: 708 health concerns all - BE signup
   Given on homepage and "Belgium" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And health all issues Joints Skin and coat Digestion Pancreatitis in "Belgium"
   And Current diet dry food international
   And Select flavour anything
   And Complete email page
   Then Dry page display all health issues in "Belgium"

  @belgium_hypo
  @roe
  Scenario: 709 hypoallergenic - BE signup
   Given on homepage and "Belgium" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients all health issues with hypoallergenic
   And Current diet dry food international
   And Select flavour anything
   And Complete email page
   Then Dry and treats page contain no hypo ingredients in "Belgium"

  @belgium_exclusions
  @roe
  @nightly_chrome_four
  Scenario: 710 excluded ingredients - BE signup
   Given on homepage and "Belgium" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health issues none and ingredients excluded wheat beef chicken soya fish dairy egg
   And Current diet dry food international
   And Select flavour anything
   And Complete email page
   Then Dry page "Belgium" contain no excluded ingredients

  @belgium_puppy
  @roe
  Scenario: 711 puppy - BE signup
   Given on homepage and "Belgium" country
   When Add "beagle" information age "0" years "2" months female not spayed purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working puppy weight "6"
   And Health issues "International" selected lamb and wheat
   And Current diet dry and wet food international
   And Current food no dry selected wet "Mini can (156g)" international
   And Select flavour anything
   And Complete email page
   Then Dry page "Belgium" contains no exclusions "Wheat" "Lamb" and no option for wet food or treats

  @belgium_pregnant
  @roe
  Scenario: 712 pregnant/nursing - BE signup
    Given on homepage and "Belgium" country
    When one dog female not spayed "pregnant"
    And is pregnant
    Then alert display for no unique recipes for pregnant dogs

  @belgium_specbreed
  @roe
  Scenario: 713 special breed - BE signup
    Given on homepage and "Belgium" country
    When Add "dogone" information age "2" years "5" months male neutered special purebreed "Dalmation"
    Then alert for restricted protein
