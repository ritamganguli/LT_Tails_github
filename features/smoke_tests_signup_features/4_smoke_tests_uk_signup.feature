@growth_regression
@uk_smoke
Feature: Sign up smoke tests

  @nightly_iphone_one
  @nightly_android_one
  @uksmoke_crossbreed_hypo
  Scenario: 1001 dry only cross-breed dominant breed - UK signup
    Given on homepage and "United Kingdom" country
    When Add "dogone" information age "2" years "5" months male neutered three crossbreed "Labrador Retriever" and "Cockapoo" and "Pomeranian"
    And Select first dominant breed go back "Pomeranian"
    And Add third breed "Beagle" and "Alapaha Blue Blood Bulldog" and "Pomeranian"
    And three crossbreed selection for dominant breed "Beagle" and "Alapaha Blue Blood Bulldog" and "Pomeranian"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no health issues with hypoallergenic UK
    And Current diet dry food
    And Current food select no brand
    And Select flavour anything
    And Complete email page for petname "breedsmokedryfood"
    Then Dry and treats page contain no hypo ingredients in "United Kingdom"

  @nightly_iphone_four
  @uk_puppy
  Scenario: 1002 dry and wet not working puppy pure breed - UK signup
    Given on homepage and "United Kingdom" country
    When Add "beagle" information age "0" years "2" months female not spayed purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working dog weight "6" just right weight
    And Health issues none and ingredients excluded lamb
    And Current diet select dry wet food and treats other food
    And Current food selected wet "Mini can (156g)"
    And Select flavour anything
    And Complete email page
    Then Dry page contain no "lamb" for puppy


  @nightly_android_three
  @uksmoke_hypo
  Scenario: 1003 unknown breed hypoallergenic resume add dog - UK signup
   Given on homepage and "United Kingdom" country
   When Add "dogone" information age "2" years "5" months male neutered unknownbreed "Giant"
   And Select gain weight motivation for dog food
   And Status no working dog weight estimate
   And Health Ingredients no health issues with hypoallergenic UK
   And Current diet dry food
   And Current food select no brand
   And Select flavour anything
   And Navigate to Home logo
   And can Continue signup
   And Complete email page
   Then Dry and treats page contain no hypo ingredients in "United Kingdom"


  @uksmoke_pregnant
  @nightly_android_four
  Scenario: 1004 pregnant nursing - UK signup
    Given on homepage and "United Kingdom" country
    When one dog female not spayed "pregnant"
    And is pregnant
    Then alert display for no unique recipes for pregnant dogs

  @nightly_iphone_one
  @nightly_android_four
  @uksmoke_twodogs
  Scenario: 1005 two dogs - UK signup
    Given on homepage and "United Kingdom" country
    When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues UK
    And Current diet select dry wet food and treats other food
    And Current food dry "Purina" selected wet "Mini can (156g)"
    And Select flavour anything
    And Complete email page
    And select dry food only Project Box and add another dog
    And Add "dogtwo" information age "3" years "5" months male neutered purebreed "labradoodle"
    When Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues UK
    And Current diet select dry wet food and treats other food
    And Current food dry "Purina" selected wet "Mini can (156g)"
    And Select flavour anything
    And select dry and wet Project Box in "United Kingdom"
    And Select no treats Project Box
    Then Pricing and pet page for "Dogtwo"

  @nightly_chrome_three
  @uksmoke_savingcomms_pref_yes
  Scenario: 1006 saving comms preferences to YES on signup - UK signup
   Given on homepage and "United Kingdom" country
   When Add "behave" information age "2" years neutered purebreed "Labrador"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues UK
   And Current diet select dry and wet food
   And Current food dry "Purina" selected wet "Mini can (156g)"
   And Select flavour anything
   Then On email selecting Yes for communication Frontyard shows the customer as contactable

  @nightly_chrome_two
  @uksmoke_savingcomms_pref_no
  Scenario: 1007 saving comms preferences to No on signup - UK signup
   Given on homepage and "United Kingdom" country
   When Add "behave" information age "2" years neutered purebreed "Labrador"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues UK
   And Current diet select dry and wet food
   And Current food dry "Purina" selected wet "Mini can (156g)"
   And Select flavour anything
   Then On email selecting No for communication Frontyard shows the customer as not contactable

  @nightly_iphone_four
  @nightly_android_three
  @uksmoke_specbreed
  Scenario: 1008 special breed - UK signup
    Given on homepage and "United Kingdom" country
    When Add "dogone" information age "2" years "5" months male neutered special purebreed "Dalmation"
    Then alert for restricted protein

  @nightly_chrome_two
  @disabled_email_button
  Scenario: 1009 disabled button on email step - UK signup
    Given on homepage and "United Kingdom" country
    When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues UK
    And Current diet dry food
    And Current food select no brand
    And Select flavour anything
    Then email step is in a disabled state

  @nightly_iphone_four
  @uksmoke_wf_flavours/textures_accordion
  Scenario: UK 1010 updating the flavours/textures accordion - UK signup
    Given on homepage and "United Kingdom" country
    When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues UK
    And Current diet select dry and wet food
    And Current food dry "Purina" selected wet "Mini can (156g)"
    And Select flavour anything
    And Complete email page
    Then Updating wet food flavours/textures displays correct wet food selection in "United Kingdom"

  @nightly_iphone_two
  @desmoke_wf_flavours/textures_accordion
  Scenario:DE 1011 updating the flavours/textures accordion - DE signup
   Given on homepage and "Germany" country
    When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues
    And Current diet select dry and wet food
    And Current food no dry selected wet "Kleine Dose (156g)"
    And Select flavour anything
    And Complete email page
    Then Updating wet food flavours/textures displays correct wet food selection in "Germany"

  @nightly_iphone_one
  @frsmoke_wf_flavours/textures_accordion
  Scenario: FR 1012 updating the flavours/textures accordion FR signup
    Given on homepage and "France" country
    When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues
    And Current diet select dry and wet food
    And Current food no dry selected wet "Mini conserve (156g)"
    And Select flavour anything
    And Complete email page
    Then Updating wet food flavours/textures displays correct wet food selection in "France"

  @nightly_iphone_four
  @uksmoke_wf_flavours/textures_eligibility
  Scenario: GB signup - 1013 ineligible flavours/textures in accordion - uk
    Given on homepage and "United Kingdom" country
    When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health issues none and ingredients excluded lamb
    And Current diet select dry and wet food
    And Current food dry "Purina" selected wet "Mini can (156g)"
    And Select flavour anything
    And Complete email page
    Then Wet food flavours/textures accordion displays correct selection in "United Kingdom"