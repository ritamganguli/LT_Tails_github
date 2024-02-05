@growth_regression
@netherlands_checkout
@signup
Feature: Netherlands Signup

  @netherlands_stripe
  @nightly_chrome_two
  @roe
  Scenario: 601 dry food stripe future date - NE signup
     Given on homepage and "Netherlands" country
     When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
     And Select gain weight motivation for dog food
     And Status no working dog weight "15"
     And Health Ingredients no issues
     And Current diet select dry and wet food pipeline
     And Current food dry "Purina" selected wet "Mini can (156g)" pipeline
     And Select flavour anything pipeline
     And Complete email page pipeline
     And select dry and wet Project Box in "Netherlands"
     And Select no treats Project Box
     And Pricing continue with card
     And Checkout international address for "Netherlands" future delivery date
     And Checkout with stripe payment details
     Then Signup completed and dutch "Ga verder naar mijn dashboard" display


  @netherlands_stripe_billing
  @roe
  @nightly_chrome_six
  Scenario: 603 Stripe with billing address - NE signup
      Given on homepage and "Netherlands" country
      When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
      And Health Ingredients no issues
      And Current diet select dry and wet food pipeline
      And Current food dry "Purina" selected wet "Mini can (156g)" pipeline
      And Select flavour anything pipeline
      And Complete email page pipeline
      And select dry and wet Project Box in "Netherlands"
      And Select no treats Project Box
      And Pricing continue with card
      And Checkout international address for "Netherlands" future delivery date
      And Checkout with stripe billing address with manual address input "NL"
      Then Signup completed and dutch "Ga verder naar mijn dashboard" display

  @netherlands_express
  @roe
  Scenario: 605 dry & wet food & dental dailies - express delivery - NE signup
     Given on homepage and "Netherlands" country
     When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
     And Select gain weight motivation for dog food
     And Status no working dog weight "15"
     And Health Ingredients no issues
     And Current diet dry and wet food international
     And Current food selected wet food "Mini can (156g)" international for "Netherlands"
     And Select flavour anything
     And Complete email page
     And select dry and wet Project Box in "Netherlands"
     And select dental dailies treats Project Box in "Netherlands"
     And Pricing continue with card
     Then Checkout international address for "Netherlands" express delivery

  @netherlands_threedogs
  @roe
  @nightly_chrome_three
  Scenario: 614 three dogs - NE signup
    Given on homepage and "Netherlands" country
    When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues
    And Current diet dry food
    And Current food select no brand
    And Select flavour anything
    And Complete email page
    And select dry food only Project Box and add another dog
    And Add "dogtwo" information age "3" years "5" months male neutered purebreed "labradoodle"
    When Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues
    And Current diet dry food
    And Current food select no brand
    And Select flavour anything
    And select dry food only order while dry food only is in current diet in "Netherlands"
    And Select no treats Project Box
    Then Pricing and pet page for "Dogtwo"
    When Add another dog from navigation page
    And Add "dogthree" information age "3" years "5" months male neutered purebreed "cockapoo"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues
    And Current diet dry food
    And Current food select no brand
    And Select flavour anything
    And select dry food only order while dry food only is in current diet in "Netherlands"
    And Select no treats Project Box
    Then Pricing and pets page with three dogs "Dogthree"

