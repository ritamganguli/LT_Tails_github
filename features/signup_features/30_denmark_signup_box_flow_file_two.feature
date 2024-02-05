@growth_regression
@denmark_checkout
Feature: Denmark Signup box flow v2


  @denmark_stripe
   @roe
  Scenario: 501 dry food stripe future date - DN signup
     Given on homepage and "Denmark" country
     When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
     And Select gain weight motivation for dog food
     And Status no working dog weight "15"
     And Health Ingredients no issues
     And Current diet dry food international
     And Select flavour anything
     And Complete email page
     And select dry food only order while dry food only is in current diet in "Denmark"
     And Select no treats Project Box
     And Pricing continue with card
     And Checkout international address for "Denmark" future delivery date
     And Checkout with stripe payment details
     Then Signup completed and "Continue to my dashboard" display


  @denmark_stripe_billing
  @roe
  Scenario: 503 Stripe with billing address - DN signup
     Given on homepage and "Denmark" country
     When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
     And Select gain weight motivation for dog food
     And Status no working dog weight "15"
     And Health Ingredients no issues
     And Current diet dry food international
     And Select flavour anything
     And Complete email page
     And select dry food only order while dry food only is in current diet in "Denmark"
     And Select no treats Project Box
     And Pricing continue with card
     And Checkout international address for "Denmark" future delivery date
     And Checkout with stripe billing address with manual address input "DK"
     Then Signup completed and "Continue to my dashboard" display


  @denmark_express
  @roe
  Scenario: 505 dry & wet food & dental dailies - express delivery - DN signup
     Given on homepage and "Denmark" country
     When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
     And Select gain weight motivation for dog food
     And Status no working dog weight "15"
     And Health Ingredients no issues
     And Current diet dry and wet food international
     And Current food selected wet food "Mini can (156g)" international for "Denmark"
     And Select flavour anything
     And Complete email page
     And select dry and wet Project Box in "Denmark"
     And select dental dailies treats Project Box in "Denmark"
     And Pricing continue with card
     Then Checkout international address for "Denmark" express delivery

  @denmark_three_dogs
  @roe
  Scenario: 514 three dogs - DN signup
      Given on homepage and "Denmark" country
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
      And select dry food only order while dry food only is in current diet in "Denmark"
      And Select no treats Project Box
      Then Pricing and pet page for "Dogtwo"
      When Add another dog from navigation page
      And Add "dogthree" information age "3" years "5" months male neutered purebreed "cockapoo"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
      And Health Ingredients no issues
      And Current diet dry food international
      And Select flavour anything
      And select dry food only order while dry food only is in current diet in "Denmark"
      And Select no treats Project Box
      Then Pricing and pets page with three dogs "Dogthree"
