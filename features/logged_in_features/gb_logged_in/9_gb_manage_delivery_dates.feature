@owner_regression
@deliveries_changedate @owner
Feature: UK - Change delivery windows and delay deliveries tests in GB store

  @nightly_chrome_one
  @loggedin_deliveries_changedate0001
  Scenario: 0001 - Change delivery date for a subscription UK via deliveries page -UK logged in
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    And Add fixed revenue for dataseed pet
    When Navigates to manage my box page
    And Change delivery date from manage my box page
    Then The manage box page is showing new delivery date on delivery card section


  @nightly_chrome_five
  @loggedin_deliveries_changedate0002
  Scenario: 0002 -Change delivery date for a subscription UK via quick links - UK logged in
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    And Add fixed revenue for dataseed pet
    When Select change delivery dates - quick links
    And Select to move the new delivery date
    Then The manage box page is showing new delivery date on delivery card section


  @nightly_chrome_one
  @loggedin_deliveries_changedate0004
  Scenario: 0004 Delay subscription for one month - UK logged in
    Given Get next delivery date from frontyard for customer with store type "active" store id "1"
    And Logged in to tails.com store "United Kingdom" with existing email
    And Add fixed revenue for dataseed pet
    When subscription is delayed for "1" month via quick links
    Then next delivery date is updated by "1" month

  @nightly_chrome_one
  @loggedin_deliveries_changedate0005
  Scenario: 0005 Delay subscription for two months - UK logged in
    Given Get next delivery date from frontyard for customer with store type "active" store id "1"
    And Logged in to tails.com store "United Kingdom" with existing email
    When subscription is delayed for "2" month via quick links
    Then next delivery date is updated by "2" month


  @nightly_chrome_one
  @loggedin_deliveries_changedate0006
  Scenario: 0006 Delay subscription for two weeks - UK logged in
    Given Get next delivery date from frontyard for customer with store type "active" store id "1"
    And Logged in to tails.com store "United Kingdom" with existing email
    When subscription is delayed for 2 weeks via quick links
    Then next delivery date is updated by 2 weeks


  @loggedin_deliveries_changedate0007
  @nightly_chrome_five
  Scenario: delivery 0007 - Change delivery date by selecting a different delivery window - UK logged in
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    And Add fixed revenue for dataseed pet
    When Select change delivery dates - quick links
    And Select to move the new delivery date
    Then The manage box page is showing new delivery date on delivery card section
