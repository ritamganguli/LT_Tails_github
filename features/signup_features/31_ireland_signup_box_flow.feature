@growth_regression
@ireland_checkout
Feature: Ireland Signup box flow v2

  @ireland_stripe
  @nightly_chrome_six
  Scenario: 01 dry food stripe - IR signup
     Given on homepage and "Ireland" country
     When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
     And Select gain weight motivation for dog food
     And Status no working dog weight "15"
     And Health Ingredients no issues
     And Current diet dry food international
     And Select flavour anything
     And Complete email page
     And select dry food only order while dry food only is in current diet in "Ireland"
     And Select no treats Project Box
     And Pricing continue with card
     And Checkout international address for "Ireland" future delivery date
     And Checkout with stripe payment details
     Then Signup completed and "Continue to my dashboard" display

