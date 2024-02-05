@owner_regression
@nightly_chrome_one
Feature: pipeline fy - 6 customer account loads on Frontyard

   Scenario: 6 customer account loads on Frontyard - UK signup
      Given A customer from "United Kingdom" customer account "active" and store "1" exist
      Then customer account loads on frontyard

