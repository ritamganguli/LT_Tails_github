@growth_regression
@austria_no_checkout
Feature: Austria Signup box flow file one - v2

  @austria_resume_dominantbreed
  @roe
  Scenario: 306 incomplete and resume signup - AU signup
   Given on homepage and "Austria" country
   When Add "dogone" information age "2" years "5" months male neutered three crossbreed "Labrador Retriever" and "Cockapoo" and "Pomchi"
   And Select first dominant breed go back "Cockapoo"
   And Add third breed "Labrador Retriever" and "Cockapoo" and "Pomchi"
   And three crossbreed selection for dominant breed "Labrador Retriever" and "Cockapoo" and "Pomchi"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet dry food international
   And Select flavour anything
   Then complete signup with email "Austria"

  @austria_partial_crossbreed
  @roe
  @nightly_chrome_four
  Scenario: 307 partial - AU signup
   Given on homepage and "Austria" country
   When Add "dogone" information age "2" years "5" months male neutered two crossbreed "Beagle" and "Pomchi"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet dry food international
   And Select flavour anything
   And Navigate to Home logo
   Then can Continue signup "Dogone"

  @austria_health_all_unknown_breed
  @roe
  Scenario: 308 health concerns all - AU signup
   Given on homepage and "Austria" country
   When Add "dogone" information age "2" years "5" months male neutered unknown breed selected "Riese (über 40 kg)" for "AT"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And health all issues Joints Skin and coat Digestion Pancreatitis in "Austria"
   And Current diet dry food international
   And Select flavour anything
   And Complete email page
   Then Dry page display all health issues in "Austria"

  @austria_hypo
  @roe
  Scenario: 309 hypoallergenic - AU signup
   Given on homepage and "Austria" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients all health issues with hypoallergenic
   And Current diet dry food international
   And Select flavour anything
   And Complete email page
  Then Dry and treats page contain no hypo ingredients in "Austria"

  @austria_exclusions
  @roe
  Scenario: 310 excluded ingredients - AU signup
   Given on homepage and "Austria" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health issues none and ingredients excluded wheat beef chicken soya fish dairy egg
   And Current diet dry food international
   And Select flavour anything
   And Complete email page
  Then Dry page "Austria" contain no excluded ingredients

  @austria_puppy
  @roe
  Scenario:311 puppy - AU signup
   Given on homepage and "Austria" country
   When Add "beagle" information age "0" years "2" months female not spayed purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working puppy weight "6"
   And Health issues "German" selected lamb and wheat
   And Current diet dry and wet food international
   And Current food no dry selected wet "Kleine Dose (156g)" international
   And Select flavour anything
   And Complete email page
   Then Dry page "Austria" contains no exclusions "Weizen" "Lammfleisch" and no option for wet food or treats

  @austria_pregnant
  @roe
  @nightly_chrome_four
  Scenario: 312 pregnant/nursing - AU signup
    Given on homepage and "Austria" country
    When one dog female not spayed "pregnant"
    And is pregnant
    Then german alert display for no unique recipes for pregnant dogs

  @austria_specbreed
  @roe
  @nightly_chrome_four
  Scenario: 313 special breed - AU signup
    Given on homepage and "Austria" country
    When Add "dogone" information age "2" years "5" months male neutered special purebreed "Dalmation"
    Then  german alert for restricted protein
