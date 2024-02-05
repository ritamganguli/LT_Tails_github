@owner_regression
@raf
Feature: RAF page link check for all stores

  @nightly_iphone_two
  @uksmoke_rafs
  Scenario: 8001 - view RAF page - UK logged in
   Given Logged in to "United Kingdom" customer account "active" and store "1"
   When Select RAF page
   Then Confirm "Share the love today" in store "GB" displays

  @nightly_iphone_three
  @frsmoke_raf
  Scenario: 8002 - view RAF page - FR logged in
   Given Logged in to "France" customer account "active" and store "3"
   When Select RAF page
   Then Confirm "Partagez votre lien" in store "FR" displays

  @nightly_iphone_two
  @desmoke_raf
  Scenario: 8003 - view RAF page - GE logged in
   Given Logged in to "Deutschland" customer account "active" and store "4"
   When Select RAF page
   Then Confirm "Jetzt persönlichen Link teilen" in store "DE" displays