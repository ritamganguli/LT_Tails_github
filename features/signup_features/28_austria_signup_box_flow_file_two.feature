@growth_regression
@austria_checkout
Feature: Austria Signup box flow file two - v2


  @austria_stripe
  @roe
  @nightly_chrome_three
  Scenario: 301 dry food stripe future date - AU signup
   Given on homepage and "Austria" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet dry food international
   And Select flavour anything
   And Complete email page
   And select dry food only order while dry food only is in current diet in "Austria"
   And Select no treats Project Box
   And Pricing continue with card
   And Checkout international address for "austria" future delivery date
   And Checkout with stripe payment details
   Then Signup completed and german "Weiter zu meinem Dashboard" display


  @austria_stripe_billing
  @roe
  @nightly_chrome_three
  Scenario: 303 Stripe with billing address - AU signup
   Given on homepage and "Austria" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet dry food international
   And Select flavour anything
   And Complete email page
   And select dry food only order while dry food only is in current diet in "Austria"
   And Select no treats Project Box
   And Pricing continue with card
   And Checkout international address for "austria" future delivery date
   And Checkout with stripe billing address with manual address input "AT"
   Then Signup completed and german "Weiter zu meinem Dashboard" display


  @austria_express
  @roe
  Scenario: 305 dry & wet food & dental dailies - express delivery  - AU signup
   Given on homepage and "Austria" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet dry and wet food international
   And Current food selected wet "Kleine Dose (156g)" austria
   And Select flavour anything
   And Complete email page
   And select dry and wet Project Box in "Austria"
   And select dental dailies treats Project Box in "Austria"
   And Pricing continue with card
   Then Checkout international address for "Austria" express delivery

  @austria_threedogs
  @roe
  Scenario: 314 three dogs - AU signup
    Given on homepage and "Austria" country
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
    And select dry food only order while dry food only is in current diet in "Austria"
    And Select no treats Project Box
    Then Pricing and pet page german for "Dogtwo"
    When Add another dog from navigation page
    And Add "dogthree" information age "3" years "5" months male neutered purebreed "cockapoo"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues
    And Current diet dry food international
    And Select flavour anything
    And select dry food only order while dry food only is in current diet in "Austria"
    And Select no treats Project Box
    Then Pricing and pets page german with three dogs "Dogthree"
