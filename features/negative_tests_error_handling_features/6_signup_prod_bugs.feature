@growth_regression
@signupbugsuk
Feature: Tests based on previous bugs that made it to production in the signup flow.


  @nightly_chrome_one
  @signupbugs.raf
  Scenario: signup prod bug- 15002 - raf link incorrect promo
    Given On RAF page and "United Kingdom" country
    When Go into signup flow raf "United Kingdom"
    Then Offer text is "Free dry food trial"




