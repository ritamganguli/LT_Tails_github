@shop_regression
@uk_ftw
@ftw_daily
Feature: UK - Flea tick and worm
Regression tests for flea tick & worm subscriptions

  @nightly_iphone_one
  @nightly_android_four
  @ftw_subscribe
   Scenario: ftw-001 subscribe flea tick and worm treatments - UK logged in
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    When Navigates to Treatment page and subscribes for FWT & validates the confirmation "You are now receiving this treatment."
    And Validates the FWT subscription header "Monthly flea, tick & worm treatment" in Delivery page
    And Validates the FWT subscription text "1 pack of Flea, Worm, Tick for Qa Champ" in View Delivery Details page
    When User unsubscribes from the treatment
    Then Validates the confirmation message "You’ve successfully unsubscribed"

  @nightly_iphone_two
  @ftw_weight_validate
  Scenario: ftw-002 validate the Treatment Price change due to Pet's weight change - UK logged in
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    When Navigates to Treatment page and subscribes for FWT & validates the confirmation "You are now receiving this treatment."
    When Navigate to pet profile page
    When Update weight and confirm
    Then Confirm feeding plan changes and verify price change text "£9.50 (increased from £9.00)"

  @nightly_iphone_two
  @nightly_android_two
  @ftw_weight_not_eligble
  Scenario: ftw-003: validate Pet made ineligible for treatment due to weight change - UK logged in
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    When Navigates to Treatment page and subscribes for FWT & validates the confirmation "You are now receiving this treatment."
    When Navigate to pet profile page
    When Update weight less than 2kg
    Then Confirm feeding plan changes and verify ineligible message "Sorry, you are no longer eligible to receive this treatment:"


