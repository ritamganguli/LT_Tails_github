@owner_regression
@owner
Feature: UK - Add new pet as existing customer

  @nightly_android_three
  @add_dog_incomplete
    Scenario: 001 Add new dog quick link takes customer to signup page - UK logged in
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    When Add a new dog using quick link
    Then Confirm "About your dog" displays on the my-dog signup page
