@growth_regression
@netherlands_no_checkout
@signup
Feature: Netherlands Signup

  @netherlands_resume_dominantbreed
  @roe
  Scenario: 606 incomplete and resume signup - NE signup
   Given on homepage and "Netherlands" country
   When Add "dogone" information age "2" years "5" months male neutered three crossbreed "Labrador Retriever" and "Cockapoo" and "Pomchi"
   And Select first dominant breed go back "Cockapoo"
   And Add third breed "Labrador Retriever" and "Cockapoo" and "Pomchi"
   And three crossbreed selection for dominant breed "Labrador Retriever" and "Cockapoo" and "Pomchi"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet dry food
   And Current food select no brand
   And Select flavour anything
   Then complete signup with email "Dutch"


  @netherlands_health_unknown_breed
  @nightly_iphone_three
  @roe
  Scenario: 607 health concerns all - NE signup
   Given on homepage and "Netherlands" country
   When Add "dogone" information age "2" years "5" months male neutered unknown breed selected "reus (40+ kg)" for "NL"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And health all issues Joints Skin and coat Digestion Pancreatitis in "Netherlands"
   And Current diet dry food
   And Current food select no brand
   And Select flavour anything
   And Complete email page
   Then Dry page display all health issues in "Netherlands"

  @netherlands_partial_crossbreed
  @nightly_chrome_six
  @roe
  Scenario: 608 partial - NE signup
   Given on homepage and "Netherlands" country
   When Add "dogone" information age "2" years "5" months male neutered two crossbreed "Beagle" and "Bulldog"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet dry food
   And Current food select no brand
   And Select flavour anything
   And Navigate to Home logo
   Then can Continue signup "Dogone"


  @netherlands_hypo
  @nightly_android_three
  Scenario: - NE signup609 hypoallergenic - NE signup
   Given on homepage and "Netherlands" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients all health issues with hypoallergenic
   And Current diet dry food
   And Current food select no brand
   And Select flavour anything
   And Complete email page
   Then Dry and treats page contain no hypo ingredients in "Netherlands"

  @netherlands_exclusions
  @nightly_iphone_three
  Scenario: 610 excluded ingredients - NE signup
   Given on homepage and "Netherlands" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health issues none and ingredients excluded wheat beef chicken soya fish dairy egg
   And Current diet dry food
   And Current food select no brand
   And Select flavour anything
   And Complete email page
   Then Dry page "Netherlands" contain no excluded ingredients

  @netherlands_puppy
  @roe
  Scenario: 611 puppy - NE signup
   Given on homepage and "Netherlands" country
   When Add "nethdog" information age "0" years "2" months female not spayed purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working puppy weight "6"
   And Health issues "Dutch" selected lamb and wheat
   And Current diet dry and wet food international
   And Current food selected wet food "Mini can (156g)" international for "Netherlands"
   And Select flavour anything
   And Complete email page
   Then Dry page "Netherlands" contains no exclusions "Tarwe" "Lam" and no option for wet food or treats

   @netherlands_pregnant
   @nightly_android_two
   @roe
   Scenario: 612 pregnant/nursing - NE signup
    Given on homepage and "Netherlands" country
    When one dog female not spayed "pregnant"
    And is pregnant
    Then netherlands alert display for no unique recipes for pregnant dogs

   @netherlands_specbreed
   @nightly_iphone_three
   @roe
   Scenario: 613 special breed - NE signup
      Given on homepage and "Netherlands" country
      When Add "dogone" information age "2" years "5" months male neutered special purebreed "Dalmatiër"
      Then netherlands alert for restricted protein
