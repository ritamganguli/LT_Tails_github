Feature: DE - Update payment method feature
  This feature will contain all scenarios for updating payment method for FR store

  # Commented out until we can fix the paypal issue on line 10
#  Scenario: payment DE 0001 - Switching existing payment method to paypal with different billing address, postcode search
#    Given Logged in to "Deutschland" customer account "active" and store "4"
#    # Translation ticket for Account Settings showing in DE - OS-2493
#    When Select Account page and confirm "Account settings" displays
#    And Select Paypal payment method
#    And Input Paypal credentials for "DE" store
#    And Select and enter a different billing address in Germany
#    And Confirm Paypal payment method update
#    #the below step is an assert only
#    When Banner "Zahlungsmethode zu PayPal geändert" is showing on account settings page
#    Then Verify Paypal account is updated on account settings page
