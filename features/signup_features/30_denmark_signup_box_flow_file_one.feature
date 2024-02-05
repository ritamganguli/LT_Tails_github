@growth_regression
@denmark_no_checkout
Feature: Denmark Signup box flow v2

  @denmark_resume
   @roe
  Scenario: 506 incomplete and resume signup - DN signup
   Given on homepage and "Denmark" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet dry food international
   And Select flavour anything
   Then complete signup with email "English"

  @denmark_partial
  @roe
  Scenario:507 partial - DN signup
   Given on homepage and "Denmark" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet dry food international
   And Select flavour anything
   And Navigate to Home logo
   Then can Continue signup "Dogone"

  @denmark_health
  @roe
  Scenario: 508 health concerns all - denmark box flow
   Given on homepage and "Denmark" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And health all issues Joints Skin and coat Digestion Pancreatitis in "Denmark"
   And Current diet dry food international
   And Select flavour anything
   And Complete email page
   Then Dry page display all health issues in "Denmark"

  @denmark_hypo
  @roe
  @nightly_chrome_four
  Scenario: 509 hypoallergenic - DN signup
   Given on homepage and "Denmark" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients all health issues with hypoallergenic
   And Current diet dry food international
   And Select flavour anything
   And Complete email page
   Then Dry and treats page contain no hypo ingredients in "Denmark"

  @denmark_exclusions
  @roe
  Scenario: 510 excluded ingredients - DN signup
   Given on homepage and "Denmark" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health issues none and ingredients excluded wheat beef chicken soya fish dairy egg
   And Current diet dry food international
   And Select flavour anything
   And Complete email page
   Then Dry page "Denmark" contain no excluded ingredients

  @denmark_puppy
  @roe
  @nightly_chrome_four
  Scenario: 511 puppy - DN signup
   Given on homepage and "Denmark" country
   When Add "beagle" information age "0" years "2" months female not spayed purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working puppy weight "6"
   And Health issues "International" selected lamb and wheat
   And Current diet dry and wet food international
   And Current food no dry selected wet "Mini can (156g)" international
   And Select flavour anything
   And Complete email page
   Then Dry page "Denmark" contains no exclusions "Wheat" "Lamb" and no option for wet food or treats

  @denmark_pregnant
  @roe
  Scenario: 512 pregnant/nursing - DN signup
    Given on homepage and "Denmark" country
    When one dog female not spayed "pregnant"
    And is pregnant
    Then alert display for no unique recipes for pregnant dogs

  @denmark_specbreed
  @roe
  Scenario: 13 special breed - DN signup
    Given on homepage and "Denmark" country
    When Add "dogone" information age "2" years "5" months male neutered special purebreed "Dalmation"
    Then alert for restricted protein
