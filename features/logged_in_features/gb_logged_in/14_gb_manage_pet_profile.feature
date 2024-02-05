@owner_regression
@profile_pages @owner
Feature: UK - Update pet profiles

  @nightly_iphone_four
  @nightly_android_four
  @profile_weight
  Scenario: 001 profile update weight - UK logged in
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    When Navigate to pet profile page
    And Update weight and condition
    And Confirm feeding plan changes
    Then Successful update notification "profile and feeding plan have been updated" is displayed on profile page

  @nightly_iphone_four
  @profile_health
  Scenario: 002 profile add health condition - UK logged in
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    When Navigate to pet profile page
    And Add health condition "Skin and coat"
    And Confirm feeding plan changes
    Then Successful update notification "profile and feeding plan have been updated" is displayed on profile page

  @nightly_iphone_four
  @profile_pancreatitis
  Scenario: 003 profile adding Pancreatitis shows exclusion message - UK logged in
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    When Navigate to pet profile page
    And Add health condition "Pancreatitis"
    And Confirm feeding plan changes
    Then Successful update notification "profile and feeding plan have been updated" is displayed on profile page

  @nightly_iphone_four
  @nightly_android_two
  @profile_exclusion
  Scenario: 004 profile add exclusion - UK logged in
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    When Navigate to pet profile page
    And Add ingredient to exclude "Chicken"
    And Confirm feeding plan changes
    Then Successful update notification "profile and feeding plan have been updated" is displayed on profile page