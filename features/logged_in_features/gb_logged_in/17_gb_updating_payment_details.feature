@owner_regression
@update_payment
@owner
Feature: UK - Update payment method feature
  This feature will contain all scenarios for updating payment method for UK store


  @nightly_android_four
  @loggedin_account_payment_card_uk_payment0001
  Scenario: 0001 payment switching existing method to card payment - UK logged in
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    When Select Account page and confirm "Account settings" displays
    And Select payment method "Stripe"
    And Add and submit stripe payment details
    #the below step is an assert only
    When Banner "Updated payment method to credit/debit card" is showing on account settings page
    Then Verify card details are updated on account settings page


  @nightly_chrome_one
  @loggedin_account_payment_paypal_uk_payment0002
  Scenario: 0002 Switch existing payment method to paypal - UK logged in
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    When Select Account page and confirm "Account settings" displays
    And Select Paypal payment method
    And Input Paypal credentials for "UK" store
    And Confirm Paypal payment method update
    #the below step is an assert only
    When Banner "Updated payment method to PayPal" is showing on account settings page
    Then Verify Paypal account is updated on account settings page


  @nightly_android_two
  @loggedin_account_payment_stripe_billing_UK_payment0003
  Scenario: 0003 Switching existing payment method to stripe with registering billing address - UK logged in
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    When Select Account page and confirm "Account settings" displays
    And Select payment method "Stripe"
    And Add and submit stripe payment details with billing address "49A Stanley Road"
    #the below step is an assert only
    When Banner "Updated payment method to credit/debit card" is showing on account settings page
    Then Verify card details are updated on account settings page

  Scenario: payment 0004 - Switching existing payment method to paypal with different billing address, postcode search- UK
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    When Select Account page and confirm "Account settings" displays
    And Select Paypal payment method
    And Input Paypal credentials for "UK" store
    And Select and enter a different billing address
    And Confirm Paypal payment method update
    #the below step is an assert only
    When Banner "Updated payment method to PayPal" is showing on account settings page
    Then Verify Paypal account is updated on account settings page

  Scenario: payment 0005 - Switching existing payment method to paypal with different billing address, manual entry - UK
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    When Select Account page and confirm "Account settings" displays
    And Select Paypal payment method
    And Input Paypal credentials for "UK" store
    And Select and enter a different billing address via manual input
    And Confirm Paypal payment method update
    # the below step is an assert only
    When Banner "Updated payment method to PayPal" is showing on account settings page
    Then Verify Paypal account is updated on account settings page