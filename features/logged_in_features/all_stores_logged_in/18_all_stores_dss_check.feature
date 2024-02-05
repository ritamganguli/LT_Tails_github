@owner_regression
@DSS_dry_food @owner
@nightly_chrome_one
Feature: Verify DSS data
  DSS is an email sent to customers prior to shipment being fulfilled and sent

  Scenario Outline: DSS 001 Get DSS data for a pet on dry food only for each store
    Given Access to "active" customer account on Frontyard in store id "<store_id>"
    When Submits request to get DSS data
    Then Dry food product title in DSS data is displayed with "<dss_dry_food_title>"

     Examples:
    | store | store_id |   dss_dry_food_title      |
    |  GB   |     1    |   Tails.com dry food      |
    |  FR   |     3    |   Croquettes tails.com    |
    |  DE   |     4    |   Tails.com Trockenfutter |
    |  IE   |     6    |   Tails.com dry food      |
    |  NL   |     9    |   Tails.com droogvoer     |
    |  AT   |     11   |   Tails.com Trockenfutter |
    |  BE   |     10   |   Tails.com dry food      |
    |  SE   |     7    |   Tails.com dry food      |
    |  DK   |     8    |   Tails.com dry food      |