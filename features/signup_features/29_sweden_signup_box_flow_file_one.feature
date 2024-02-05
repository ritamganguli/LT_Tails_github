@growth_regression
@sweden_no_checkout
Feature: Sweden Signup box flow v2

  @sweden_incomplete_resume
  @roe
  @nightly_chrome_four
  Scenario: 806 incomplete and resume signup - SW signup
   Given on homepage and "Sweden" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet dry food international
   And Select flavour anything
   Then complete signup with email "English"

  @sweden_partial
  @roe
  Scenario: 807 partial - SW signup
   Given on homepage and "Sweden" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet dry food international
   And Select flavour anything
   And Navigate to Home logo
   Then can Continue signup "Dogone"

  @sweden_health
  @roe
  Scenario: 808 health concerns all - SW signup
   Given on homepage and "Sweden" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And health all issues Joints Skin and coat Digestion Pancreatitis in "Sweden"
   And Current diet dry food international
   And Select flavour anything
   And Complete email page
   Then Dry page display all health issues in "Sweden"

  @sweden_hypo
  @roe
  Scenario: 809 hypoallergenic - SW signup
   Given on homepage and "Sweden" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients all health issues with hypoallergenic
   And Current diet dry food international
   And Select flavour anything
   And Complete email page
   Then Dry and treats page contain no hypo ingredients in "Sweden"

  @sweden_exclusions
  @roe
  Scenario: 810 excluded ingredients - SW signup
   Given on homepage and "Sweden" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health issues none and ingredients excluded wheat beef chicken soya fish dairy egg
   And Current diet dry food international
   And Select flavour anything
   And Complete email page
   Then Dry page contain no "Wheat" "Beef" "Chicken" "Soya" "Fish" "Dairy" "Egg"

  @sweden_puppy
  @roe
  Scenario: 811 puppy - SW signup
   Given on homepage and "Sweden" country
   When Add "swedendog" information age "0" years "2" months female not spayed purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working puppy weight "6"
   And Health issues "International" selected lamb and wheat
   And Current diet dry and wet food international
   And Current food no dry selected wet "Mini can (156g)" international
   And Select flavour anything
   And Complete email page
   Then Dry page "Sweden" contains no exclusions "Wheat" "Lamb" and no option for wet food or treats

  @sweden_pregnant
  @roe
  Scenario: 812 pregnant/nursing - SW signup
    Given on homepage and "Sweden" country
    When one dog female not spayed "pregnant"
    And is pregnant
    Then alert display for no unique recipes for pregnant dogs

  @sweden_specbreed
  @roe
  Scenario: 813 special breed - SW signup
    Given on homepage and "Sweden" country
    When Add "dogone" information age "2" years "5" months male neutered special purebreed "Dalmation"
    Then alert for restricted protein
