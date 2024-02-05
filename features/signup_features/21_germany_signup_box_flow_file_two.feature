@growth_regression
@germany_checkout
@signup
Feature: Germany Signup

   @germany_stripe_future
   @nightly_android_two
  Scenario: 201 dry food future date stripe - DE signup
   Given on homepage and "Germany" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet select dry and wet food pipeline
   And Current food dry "Purina" selected wet "Mini can (156g)" pipeline
   And Select flavour anything pipeline
   And Complete email page pipeline
   And select dry food only wet current diet pipeline in "Germany"
   And select dental dailies treats Project Box in "Germany"
   And Pricing continue with card
   And Checkout international address for "Germany" future delivery date
   And Checkout with stripe payment details
   Then Signup completed and german "Weiter zu meinem Dashboard" display

  @nightly_chrome_five
  @germany_stripe_billing
  Scenario: 203 Stripe with billing address - DE signup
   Given on homepage and "Germany" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet select dry and wet food pipeline
   And Current food dry "Purina" selected wet "Mini can (156g)" pipeline
   And Select flavour anything pipeline
   And Complete email page pipeline
   And select dry food only wet current diet pipeline in "Germany"
   And select dental dailies treats Project Box in "Germany"
   And Pricing continue with card
   And Checkout international address for "Germany" future delivery date
   And Checkout with stripe billing address with manual address input "DE"
   Then Signup completed and german "Weiter zu meinem Dashboard" display

  @germany_express
  @nightly_android_one
  Scenario: 205 dry & wet food & dental dailies - express delivery - DE signup
   Given on homepage and "Germany" country
   When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
   And Select gain weight motivation for dog food
   And Status no working dog weight "15"
   And Health Ingredients no issues
   And Current diet select dry and wet food pipeline
   And Current food dry "Purina" selected wet "Mini can (156g)" pipeline
   And Select flavour anything pipeline
   And Complete email page pipeline
   And select dry food only wet current diet pipeline in "Germany"
   And select dental dailies treats Project Box in "Germany"
   And Pricing continue with card
   Then Checkout international address for "Germany" express delivery

  @germany_threedogs
  Scenario:214 three dogs - DE signup
    Given on homepage and "Germany" country
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
    And select dry food only order while dry food only is in current diet in "Germany"
    And Select no treats Project Box
    Then Pricing and pet page german for "Dogtwo"
    When Add another dog from navigation page
    And Add "dogthree" information age "3" years "5" months male neutered purebreed "cockapoo"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues
    And Current diet dry food
    And Current food select no brand
    And Select flavour anything
    And select dry food only order while dry food only is in current diet in "Germany"
    And Select no treats Project Box
    Then Pricing and pets page german with three dogs "Dogthree"
