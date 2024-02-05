@growth_regression
@france_checkout
@signup
Feature: France Signup


  @france_stripe
  @nightly_android_two
  Scenario: 101 dry food stripe future date - FR signup
     Given on homepage and "France" country
     When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
     And Select gain weight motivation for dog food
     And Status no working dog weight "15"
     And Health Ingredients no issues
     And Current diet select dry and wet food pipeline
     And Current food dry "Purina" selected wet "Mini can (156g)" pipeline
     And Select flavour anything pipeline
     And Complete email page pipeline
     And select dry and wet Project Box FR
     And Select no treats Project Box
     And Pricing continue with card
     And Checkout address for France future delivery date


  @france_stripe_billing
  @nightly_chrome_two
  Scenario: 103 Stripe with billing address - FR signup
     Given on homepage and "France" country
     When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
     And Select gain weight motivation for dog food
     And Status no working dog weight "15"
     And Health Ingredients no issues
     And Current diet select dry and wet food pipeline
     And Current food dry "Purina" selected wet "Mini can (156g)" pipeline
     And Select flavour anything pipeline
     And Complete email page pipeline
     And select dry and wet Project Box FR
     And Select no treats Project Box
     And Pricing continue with card
     And Checkout address for France future delivery date
     And Checkout with stripe billing address with manual address input "FR"
     Then Signup completed and france "Continuer vers mon tableau de bord" display


  @france_express
  @nightly_android_one
  Scenario: 105 dry & wet food & dental dailies - express delivery - FR signup
     Given on homepage and "France" country
     When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
     And Select gain weight motivation for dog food
     And Status no working dog weight "15"
     And Health Ingredients no issues
     And Current diet select dry and wet food pipeline
     And Current food dry "Purina" selected wet "Mini can (156g)" pipeline
     And Select flavour anything pipeline
     And Complete email page pipeline
     And select dry and wet Project Box FR
#     And Select no treats Project Box
     And select dental dailies treats Project Box in "France"
     And Pricing continue with card
     Then Checkout address for France express delivery


  @france_threedogs
  @nightly_chrome_two
  Scenario: 114 three dogs - FR signup
    Given on homepage and "France" country
    When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues UK
    And Current diet select dry wet food and treats other food
    And Current food dry "Purina" selected wet "Mini can (156g)"
    And Select flavour anything
    And Complete email page
    And select dry food only Project Box and add another dog
    And Add "dogtwo" information age "3" years "5" months male neutered purebreed "labradoodle"
    When Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues UK
    And Current diet select dry wet food and treats other food
    And Current food dry "Purina" selected wet "Mini can (156g)"
    And Select flavour anything
    And select dry and wet Project Box in "France"
    And Select no treats Project Box
    When Add another dog from pricing page
    And Add "dogthree" information age "3" years "5" months male neutered purebreed "cockapoo"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues UK
    And Current diet select dry wet food and treats other food
    And Current food dry "Purina" selected wet "Mini can (156g)"
    And Select flavour anything
    And select dry and wet Project Box in "France"
    And Select no treats Project Box
    Then Pricing and pets page with three dogs "Dogthree"
