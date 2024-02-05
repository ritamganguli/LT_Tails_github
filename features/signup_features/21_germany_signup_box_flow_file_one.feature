@growth_regression
@germany_no_checkout_feature
@signup
Feature: Germany Signup


  @germany_resume
  @nightly_chrome_six
  Scenario: 206 incomplete and resume signup - DE signup
    Given on homepage and "Germany" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet dry food
   And Current food select no brand
   And Select flavour anything
   Then complete signup with email "Germany"

  @germany_partial
  @nightly_chrome_three
  Scenario: 207 partial - DE signup
   Given on homepage and "Germany" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet dry food
   And Current food select no brand
   And Select flavour anything
   And Navigate to Home logo
   Then can Continue signup "Dogone"

  @germany_health
  @nightly_iphone_three
  Scenario: 208 health concerns all - DE signup
   Given on homepage and "Germany" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And health all issues Joints Skin and coat Digestion Pancreatitis in "Germany"
   And Current diet dry food
   And Current food select no brand
   And Select flavour anything
   And Complete email page
   Then Dry page display all health issues in "Germany"


  @germany_hypo
  @nightly_iphone_three
  Scenario: 209 hypoallergenic - DE signup
   Given on homepage and "Germany" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients all health issues with hypoallergenic
   And Current diet dry food
   And Current food select no brand
   And Select flavour anything
   And Complete email page
  Then Dry and treats page contain no hypo ingredients in "Germany"

   @germany_exclusions
   @nightly_iphone_three
   Scenario: 210 excluded ingredients - DE signup
   Given on homepage and "Germany" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health issues none and ingredients excluded wheat beef chicken soya fish dairy egg
   And Current diet dry food
   And Current food select no brand
   And Select flavour anything
   And Complete email page
   Then Dry page "Germany" contain no excluded ingredients

  @germany_puppy
  @nightly_iphone_three
  Scenario: 211 puppy - DE signup
   Given on homepage and "Germany" country
   When Add "dedog" information age "0" years "2" months female not spayed purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working puppy weight "6"
   And Health issues "German" selected lamb and wheat
   And Current diet select dry and wet food
   And Current food no dry selected wet "Kleine Dose (156g)"
   And Select flavour anything
   And Complete email page
   Then Dry page "Germany" contains no exclusions "Weizen" "Lammfleisch" and no option for wet food or treats

  @germany_pregnant
   @nightly_iphone_three
  Scenario: 212 pregnant/nursing - DE signup
    Given on homepage and "Germany" country
    When one dog female not spayed "pregnant"
    And is pregnant
    Then  german alert display for no unique recipes for pregnant dogs

  @germany_specbreed
  @nightly_iphone_three
  Scenario:213 special breed - DE signup
    Given on homepage and "Germany" country
    When Add "dogone" information age "2" years "5" months male neutered special purebreed "Dalmation"
    Then  german alert for restricted protein

