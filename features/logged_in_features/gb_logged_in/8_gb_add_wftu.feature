#@shop_regression
#@wetf
#@nightly_chrome_three
#  Flow changed
#Feature: UK Add Wet Food Top Up order
#  This feature is to validate all scenarios on Adding Wet Food Top Up order for logged in customer
#
##  Product = Rich Poultry and Game Hotpot with Duck and Carrots
#  Background: Adding wet food to a customer prior to wet food topup
#    Given Logged in to "United Kingdom" customer account "active" and store "1"
#    When Customer navigates to wet food shop
#    And Updates Wet Food Portion
#    And Adds trays to wet food selection
#    And Navigates to manage my box page from Dashboard
#    And Change delivery date from manage my box page
#
#  https://tailscom.atlassian.net/browse/QA-918
#  @broken
#  Scenario: 001 Adding Wet Food Top Up successfully and validate it - UK logged in
#    When Customer Orders Extra Wet Food
#    Then Validate Wet Food being added in upcoming deliveries




