Feature: FR - Update payment method feature
  This feature will contain all scenarios for updating payment method for FR store

#  Commented out until we can fix the paypal issue on line 9
#  Scenario: payment FR 0001 - Switching existing payment method to paypal with different billing address, postcode search
#    Given Logged in to "France" customer account "active" and store "3"
#    When Select Account page and confirm "Paramètres du compte" displays
#    And Select Paypal payment method
#    And Input Paypal credentials for "FR" store
#    And Select and enter a different billing address in France
#    And Confirm Paypal payment method update
#    #the below step is an assert only
#    When Banner "Votre méthode de paiement a bien été mise à jour" is showing on account settings page
#    Then Verify Paypal account is updated on account settings page