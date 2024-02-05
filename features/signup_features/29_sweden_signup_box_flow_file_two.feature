@growth_regression
@sweden_checkout
Feature: Sweden Signup box flow v2

  @sweden_stripe
  @roe
  Scenario: SW signup - 801 dry food stripe future date - SW signup
   Given on homepage and "Sweden" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet dry food international
   And Select flavour anything
   And Complete email page
   And select dry food only order while dry food only is in current diet in "Sweden"
   And Select no treats Project Box
   And Pricing continue with card
   And Checkout international address for "Sweden" future delivery date
   And Checkout with stripe payment details
   Then Signup completed and "Continue to my dashboard" display


  @sweden_stripe_billing
  @roe
  @nightly_chrome_four
  Scenario: SW signup-803 Stripe with billing address - SW signup
   Given on homepage and "Sweden" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet dry food international
   And Select flavour anything
   And Complete email page
   And select dry food only order while dry food only is in current diet in "Sweden"
   And Select no treats Project Box
   And Pricing continue with card
   And Checkout international address for "Sweden" future delivery date
   And Checkout with stripe billing address with manual address input "SE"
   Then Signup completed and "Continue to my dashboard" display

  @sweden_express
  @roe
   Scenario: SW signup - 805 dry & wet food & dental dailies - express delivery stripe - SW signup
     Given on homepage and "Sweden" country
     When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
     And Select gain weight motivation for dog food
     And Status no working dog weight "15"
     And Health Ingredients no issues
     And Current diet dry and wet food international
     And Current food selected wet food "Mini can (156g)" international for "Sweden"
     And Select flavour anything
     And Complete email page
     And select dry and wet Project Box in "Sweden"
     And select dental dailies treats Project Box in "Sweden"
     And Pricing continue with card
     Then Checkout international address for "Sweden" express delivery


  @sweden_threedogs
  @roe
  Scenario: 814 three dogs - SW signup
    Given on homepage and "Sweden" country
    When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues
    And Current diet dry food international
    And Select flavour anything
    And Complete email page
    And select dry food only Project Box and add another dog
    And Add "dogtwo" information age "3" years "5" months male neutered purebreed "labradoodle"
    When Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues
    And Current diet dry food international
    And Select flavour anything
    And select dry food only order while dry food only is in current diet in "Sweden"
    And Select no treats Project Box
    Then Pricing and pet page for "Dogtwo"
    When Add another dog from navigation page
    And Add "dogthree" information age "3" years "5" months male neutered purebreed "cockapoo"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues
    And Current diet dry food international
    And Select flavour anything
    And select dry food only order while dry food only is in current diet in "Sweden"
    And Select no treats Project Box
    Then Pricing and pets page with three dogs "Dogthree"
