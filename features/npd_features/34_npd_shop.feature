Feature: NPD tests for shop
  Adding and removing products from the shop via the PLP and PDP - not to be included in nightly run

  Scenario: 200001 - existing signup GB - add product via quick add in shop
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    And Add fixed revenue for dataseed pet
    When Navigates to Shop page
    And Adds "Poo bags" product
    And Navigates to manage my box page from shop
    Then "Poo Bags" product is displayed in the delivery

  Scenario: 200002 - existing signup - product not showing in shop
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    And Add fixed revenue for dataseed pet
    When Navigates to Shop page
    Then "Natürliche Kausnacks" product is not displayed in the shop

  Scenario: 200003 - existing signup - add via PDP
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    And Add fixed revenue for dataseed pet
    When Navigates to Shop page
    And Navigates to PDP for "Poo Bags" product
    And Adds product on the PDP
    And Navigates to manage my box page from shop
    Then "Poo Bags" product is displayed in the delivery

  Scenario: 200004 - existing signup - remove via PDP
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    And Add fixed revenue for dataseed pet
    When Navigates to Shop page
    And Navigates to PDP for "Poo Bags" product
    And Adds product on the PDP
    And Navigates to manage my box page from shop
    And Navigates to Shop page
    And Navigates to PDP for "Poo Bags" product when in subscription
    And Customer removes product
    And Navigates to manage my box page from shop
    Then "Poo Bags" product is not displayed in the delivery