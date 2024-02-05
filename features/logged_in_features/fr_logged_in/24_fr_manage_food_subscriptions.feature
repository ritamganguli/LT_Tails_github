@owner_regression
@owner
@logged_de_fr
Feature: FR - Restart, pause and cancel deliveries

  @smoke_cancel_account_fr
  @nightly_chrome_two
  Scenario: 3008 cancel account - FR logged in

    Cancelling the account
    Given Logged in to "France" customer account "active" and store "3"
    When Click cancel in the quick links section for "France"
    And Select the food as reason for cancelling and confirm
    Then Account cancelled and "Livraisons annulées" displays