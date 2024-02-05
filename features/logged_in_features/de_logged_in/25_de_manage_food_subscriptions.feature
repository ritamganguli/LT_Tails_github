@owner_regression
@owner
Feature: DE - Restart, pause and cancel deliveries

  @cancel_account_de
  @nightly_iphone_two
  Scenario: 3007 cancel account - DE logged in
    Cancelling the account
    Given Logged in to "Deutschland" customer account "active" and store "4"
    When Click cancel in the quick links section for "Germany"
    And Select the food as reason for cancelling and confirm
    Then Account cancelled and "Lieferungen storniert" displays