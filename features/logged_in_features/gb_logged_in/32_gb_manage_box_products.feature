@owner_regression
@owner
Feature: UK - Manage box products new next delivery page


  @nightly_android_one
  @manage_box
  Scenario: 001 Manage box page verify dry food line item is displayed   - UK logged in
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    And Add fixed revenue for dataseed pet
    When Select deliveries page and confirm "Scheduled Deliveries" displays
    And View full delivery details
    Then Confirm dry food item "Qa Champ’s tailor-made dry food" displays on manage box page