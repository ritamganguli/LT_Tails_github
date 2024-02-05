@owner_regression
@pipeline_dss
@pipe
Feature: pipeline DSS -7 - Delivery shipping soon emails

  @nightly_chrome_one
  Scenario: 7 Get DSS data for a pet on dry food only - pipeline DSS
    Given Access to "active" customer account on Frontyard in store id "1"
    When Submits request to get DSS data
    Then Dry food product title in DSS data is displayed with "Tails.com dry food"