@owner_regression
@loggedin_account_deliverydetails
@owner
Feature: UK - Updating delivery details
  Updating delivery information on accounts page for UK customers

  Background:
     Given Logged in to "United Kingdom" customer account "active" and store "1"
     When Select Account page and confirm "Account settings" displays

  @nightly_android_one
  @deliverydetails_deliveryaddress_uk
   Scenario: 0001 Change delivery address for UK deliveries - UK logged in
    When Update delivery address "49A Stanley Road"
    Then Confirm address "49A Stanley Road" displays

  @nightly_android_three
  @deliverydetails_deliveryservice_uk
  Scenario: 0002 Change delivery service for UK deliveries - UK logged in
    When Update delivery service to DPD
    Then Confirm delivery service is checked

  @nightly_android_two
  @deliverydetails_deliveryinstructions_uk
  Scenario: 0003 Add delivery instructions for UK deliveries - UK logged in
    When Update delivery instructions to "With receptionist"
    Then Confirm delivery instruction is "With receptionist"

  @nightly_android_two
  @deliverydetails_mobilenumber_uk
   Scenario: 0004 Change mobile number for UK deliveries - UK logged in
    When Update mobile number to use country code "44" and phone number "7549724114"
    Then Confirm updated mobile number is "7549724114"
