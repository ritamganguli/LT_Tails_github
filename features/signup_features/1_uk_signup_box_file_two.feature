@growth_regression
@uk_checkout
@signup
Feature: UK Signup - uk box flow


#  @nightly_chrome_one
#  @broken
#  Scenario: 002 dry & wet food paypal - UK signup
# https://tailscom.atlassian.net/browse/QA-696
#    Given on homepage and "United Kingdom" country
#    When Add "android" information age "2" years "5" months male neutered purebreed "Beagle"
#    And Select gain weight motivation for dog food
#    And Status no working dog weight "15"
#    And Health Ingredients no issues UK
#    And Current diet select dry and wet food
#    And Current food no dry selected wet "Mini can (156g)"
#    And Select flavour anything
#    And Complete email page
#    And select dry and wet in United Kingdom while dry and wet in current diet
#    And Select no treats Project Box
#    And Pricing continue with Paypal payment method "checkout_english"
#    https://tailscom.atlassian.net/browse/QA-696 Paypal updated UI & Functionality
#    And Input Paypal credentials for "UK" store
#    And Checkout address postcode "TW92SS" future delivery date
#    And checkout securely
#    Then Signup completed and "Continue to my dashboard" display


  @uk_stripe_billing
  @nightly_android_three
  Scenario: 003 stripe with billing address - UK signup
    Given on homepage and "United Kingdom" country
    When Add "dogone" information age "2" years "5" months male neutered unknownbreed "Giant"
    And Select gain weight motivation for dog food
    And Status no working dog weight estimate
    And Health Ingredients no issues UK
    And Current diet dry food
    And Current food select no brand
    And Select flavour anything
    And Complete email page
    And select dry food only order while dry food only is in current diet in "United Kingdom"
    And Select no treats Project Box
    And Pricing continue with card
    And Checkout address postcode "TW92SS" future delivery date
    And Checkout with stripe billing address with post code lookup "UK"
    Then Signup completed and "Continue to my dashboard" display

  @uk_express
  @nightly_chrome_two
  Scenario: 005 dry & wet food & dental dailies express delivery - UK signup
    Given on homepage and "United Kingdom" country
    When Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues UK
    And Current diet select dry and wet food
    And Current food no dry selected wet "Mini can (156g)"
    And Select flavour anything
    And Complete email page
    And select dry and wet in United Kingdom while dry and wet in current diet
    And select dental dailies treats Project Box in "United Kingdom"
    Then pricing page with "Dental dailies"

  @uk_threedogs
#  @nightly_iphone_one
  Scenario: 017 three dogs - UK signup
    Given on homepage and "United Kingdom" country
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
    And select dry and wet Project Box in "United Kingdom"
    And Select no treats Project Box
    When Add another dog from pricing page
    And Add "dogthree" information age "3" years "5" months male neutered purebreed "cockapoo"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues UK
    And Current diet select dry wet food and treats other food
    And Current food dry "Purina" selected wet "Mini can (156g)"
    And Select flavour anything
    And select dry and wet Project Box in "United Kingdom"
    And Select no treats Project Box
    Then Pricing and pets page with three dogs "Dogthree"

