#@shop_regression
#@wetfood
#
#Feature: UK - Add Wet food successfully & validate customer is directed to the correct shop
#  This feature is to add wet food through Manual/Auto WF shop for logged-in/new customer and verify customer is directed to respective WF shop through Shops page

#  @nightly_chrome_three
#  @add_wetf_loogedin_dashboard
#  https://tailscom.atlassian.net/browse/QA-918
#  @broken
#  Scenario: 001 - Add Wet Food for logged-in customer through Dashboard & validate customer reaches Manual shop
#    Given Logged in to "United Kingdom" customer account "active" and store "1"
#    When Customer navigates to wet food shop
#    And Updates Wet Food Portion
#    And Adds trays to wet food selection
#    When Navigates to shop page & clicks on Wet food
#    Then Customer should be directed to Manual Shop
#
#  @nightly_chrome_three
#  @add_wetf_loogedin_shops
#  Scenario: 002 - Add Wet Food for logged-in customer through Shops & validate customer reaches Manual shop
#  Given Logged in to "United Kingdom" customer account "active" and store "1"
#    When Customer navigates to wet food shop
#    And Updates Wet Food Portion
#    And Adds trays to wet food selection
#    When Customer clicks on update wet food
#    Then Customer should be directed to Manual Shop


#  @nightly_chrome_three
#  @add_wetf_loogedin_auto_shops
#  Wet food flow change
#  Scenario: 003 - Add WF during signup & validate customer reaches Auto shop
#    Given on homepage and "United Kingdom" country
#    When Add "dogone" information age "2" years "5" months male neutered unknownbreed "Giant"
#    And Select gain weight motivation for dog food
#    And Status no working dog weight estimate
#    And Health Ingredients no issues UK
#    And Current diet select dry and wet food
#    And Current food no dry selected wet "Mini can (156g)"
#    And Select flavour anything
#    And Complete email page
#    And select dry and wet in United Kingdom while dry and wet in current diet
#    And Select no treats Project Box
#    And Pricing continue with card
#    And Checkout address postcode "TW92SS" future delivery date
#    And Checkout with stripe billing address with post code lookup "UK"
#    Then Signup completed and "Continue to my dashboard" display
#    When Navigates to shop page & clicks on Wet food
#    Then Customer should be directed to Auto Shop

 