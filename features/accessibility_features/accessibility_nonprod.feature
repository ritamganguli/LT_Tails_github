@accessibility_nonprod
Feature: Conduct Accessibility testing nonprod
  # To perform accessibility audit on the critical paths - Signup, update payment, shopping.


  @accessibility_signup_nonprod
  Scenario: AA - 001 Signup nonprod workflow_1 GB Accessibility signup
    Given on homepage and "United Kingdom" country conduct Accessibility audit
    When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle" conduct Accessibility audit
    And Select gain weight motivation for dog food conduct Accessibility audit
    And Status no working dog weight "15" conduct Accessibility audit
    And Health Ingredients no issues UK conduct Accessibility audit
    And Current diet select dry and wet food conduct Accessibility audit
    And Current food no dry selected wet "Mini can (156g)" conduct Accessibility audit
    And Select flavour anything conduct Accessibility audit
    And Complete email page conduct Accessibility audit
    And select dry and wet food Project Box in "United Kingdom" conduct accessibility audit
    And Select no treats Project Box conduct Accessibility audit
    And Pricing continue with card conduct Accessibility audit
    Then Checkout with remote postcode "PH106LP" conduct Accessibility audit