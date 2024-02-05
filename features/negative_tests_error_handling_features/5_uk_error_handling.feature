@growth_regression
@uk_errorhandling
Feature: Tests to capture the error handling within signup and logged in.

  @nightly_chrome_one
  @uk_errorhandle_weight
  Scenario: 34001 - invalid weight entry errorhandle - GB signup
    Given on homepage and "United Kingdom" country
    When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working dog weight "35" just right weight
    Then Error message with "considerably higher" is displayed on the weight step

  @nightly_chrome_one
  @uk_errorhandle_wetfood
  Scenario: 34002 - too much wet food in feeding plan errorhandle - GB signup
    Given on homepage and "United Kingdom" country
    When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues UK
    And Current diet select dry and wet food
    And Current food no dry selected wet "Giant can (1200g)"
    Then Error message with "amount of wet food you have selected exceeds" displayed on current food step