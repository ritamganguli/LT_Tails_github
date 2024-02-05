
@lighthouse
@lighthouse_staging_feature
Feature: Staging UK Signup and logged in lighthouse reporting

    For all the collected audit metrics in this lighthouse test feature the thresholds are set as follows: First Contentful Paint (FCP) = 7s, Largest Contentful Paint(LCP) = 7s,
    Speed Index (SI) = 5.8 category, Performance 100 %


  @lighthouse_signup_stripe_shop_staging
   Scenario: 01-lh full dry wet and treats stripe - GB Lighthouse signup nonprod
      Given on homepage and "United Kingdom" country lighthouse "none"
      When Add "lighthouse" information age "2" year neutered purebreed "Labrador Retriever" lighthouse "avg audit"
       And Select gain weight motivation for dog food lighthouse "avg audit"
      And performance status no working dog weight "15" and lighthouse "avg audit"
      And Health Ingredients no issues lighthouse "avg audit"
      And Current diet select dry wet food and treats other food lighthouse "avg audit"
      And lighthouse current food dry "Purina" selected wet "Mini can (156g)" lighthouse "avg audit"
      And Select flavour anything lighthouse "avg audit"
      And Complete email page lighthouse "avg audit"
      And performance select dry and wet Project Box lighthouse "avg audit"
      And Select no treats Project Box lighthouse "avg audit"
      And Pricing continue with card lighthouse "avg audit"
      And Checkout address postcode "TW92SS" express delivery date lighthouse "avg audit"
      And Checkout with stripe payment details lighthouse "avg audit"
      Then Signup completed and "Continue to my dashboard" display lighthouse "avg audit"
      Then Performance check shop page load for "We recommend" products lighthouse "avg audit"


   @lighthouse_staging
   @lighthouse_breed
   Scenario: 02-lh mydog and breed avg audit load - GB Lighthouse signup nonprod
      Given on homepage and "United Kingdom" country lighthouse "none"
      When Add "ligthouse" information age "2" year neutered purebreed "Labrador Retriever" lighthouse "avg audit"

   @lighthouse_staging
   @lighthouse_motivation
   Scenario: 03-lh motivation avg audit load - GB Lighthouse signup nonprod
      Given on homepage and "United Kingdom" country
      When Add "ligthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food lighthouse "avg audit"

   @lighthouse_staging
   @lighthouse_weight
   Scenario: 04-lh weight avg audit load - GB Lighthouse signup nonprod
      Given on homepage and "United Kingdom" country
      When Add "ligthouse" information age "2" years neutered purebreed "Labrador Retriever" lighthouse "none"
      And Select gain weight motivation for dog food
      And performance status no working dog weight "15" and lighthouse "avg audit"

   @lighthouse_staging
   @lighthouse_health
   Scenario: 05-lh health avg audit load - GB Lighthouse signup nonprod
      Given on homepage and "United Kingdom" country
      When Add "ligthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
       And Health Ingredients no issues lighthouse "avg audit"

   @lighthouse_staging
   @lighthouse_box_dry
   Scenario: 06-lh box dry avg audit load - GB Lighthouse signup nonprod
      Given on homepage and "United Kingdom" country
      When Add "ligthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
       And Health Ingredients no issues
       And Current diet select dry wet food and treats other food lighthouse "avg audit"

   @lighthouse_staging
   @lighthouse_food
   Scenario: 07-lighthouse food avg audit load - GB Lighthouse signup nonprod
      Given on homepage and "United Kingdom" country
      When Add "ligthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
       And Health Ingredients no issues
       And Current diet select dry wet food and treats other food lighthouse "avg audit"

   @lighthouse_staging
   @lighthouse_current_food
   Scenario: 08-lh current food avg audit load - GB Lighthouse signup nonprod
      Given on homepage and "United Kingdom" country
      When Add "ligthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
      And Health Ingredients no issues
      And Current diet select dry wet food and treats other food
      And lighthouse current food dry "Purina" selected wet "Mini can (156g)" lighthouse "avg audit"

   @lighthouse_staging
   @lighthouse_flavour
   Scenario: 09-lh current flavour avg audit load - GB Lighthouse signup nonprod
      Given on homepage and "United Kingdom" country
      When Add "ligthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
      And Health Ingredients no issues
      And Current diet select dry wet food and treats other food
      And lighthouse current food dry "Purina" selected wet "Mini can (156g)" lighthouse "none"
      And Select flavour anything lighthouse "avg audit"

  @lighthouse_staging @lighthouse_email
  Scenario: 10-lh current flavour avg audit load - GB Lighthouse signup nonprod
    Given on homepage and "United Kingdom" country
    When Add "ligthouse" information age "2" years neutered purebreed "Labrador Retriever"
    And Select gain weight motivation for dog food
    And Status no working dog weight "15"
    And Health Ingredients no issues
    And Current diet select dry wet food and treats other food
    And lighthouse current food dry "Purina" selected wet "Mini can (156g)" lighthouse "none"
    And Select flavour anything
    And Complete email page lighthouse "avg audit"

   @lighthouse_staging
   @lighthouse_box_staging
   Scenario: 11-lh dry wet avg audit load - GB Lighthouse signup nonprod
      Given on homepage and "United Kingdom" country
      When Add "ligthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
      And Health Ingredients no issues
      And Current diet select dry wet food and treats other food
      And lighthouse current food dry "Purina" selected wet "Mini can (156g)" lighthouse "none"
      And Select flavour anything
      And Complete email page
      And performance select dry and wet Project Box lighthouse "avg audit"

   @lighthouse_staging
   @lighthouse_box_treat
   Scenario: 12-lh treats avg audit load - GB Lighthouse signup nonprod
      Given on homepage and "United Kingdom" country
      When Add "ligthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
      And Health Ingredients no issues
      And Current diet select dry wet food and treats other food
      And lighthouse current food dry "Purina" selected wet "Mini can (156g)" lighthouse "none"
      And Select flavour anything
      And Complete email page
      And select dry and wet Project Box in "United Kingdom"
      And Select no treats Project Box lighthouse "avg audit"

   @lighthouse_staging
   @lighthouse_pricing
   Scenario: 13-lh pricing avg audit load - GB Lighthouse signup nonprod
      Given on homepage and "United Kingdom" country
      When Add "ligthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
      And Health Ingredients no issues
      And Current diet select dry wet food and treats other food
      And lighthouse current food dry "Purina" selected wet "Mini can (156g)" lighthouse "none"
      And Select flavour anything
      And Complete email page
      And select dry and wet Project Box in "United Kingdom"
      And Select no treats Project Box
       And Pricing continue with card lighthouse "avg audit"

   @lighthouse_staging
   @lighthouse_address
   Scenario: 14-lh checkout address avg audit load - GB Lighthouse signup nonprod
      Given on homepage and "United Kingdom" country
      When Add "ligthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
      And Health Ingredients no issues
      And Current diet select dry wet food and treats other food
      And lighthouse current food dry "Purina" selected wet "Mini can (156g)" lighthouse "none"
      And Select flavour anything
      And Complete email page
      And select dry and wet Project Box in "United Kingdom"
      And Select no treats Project Box
      And Pricing continue with card
      And Checkout address postcode "TW92SS" express delivery date lighthouse "avg audit"

   @lighthouse_staging
   @lighthouse_stripe
   Scenario: 15-lh stripe avg audit load - GB Lighthouse signup nonprod
      Given on homepage and "United Kingdom" country
      When Add "ligthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
      And Health Ingredients no issues
      And Current diet select dry wet food and treats other food
      And lighthouse current food dry "Purina" selected wet "Mini can (156g)" lighthouse "none"
      And Select flavour anything
      And Complete email page
      And select dry and wet Project Box in "United Kingdom"
      And Select no treats Project Box
      And Pricing continue with card
      And Checkout address postcode "TW92SS" future delivery date
      And Checkout with stripe payment details lighthouse "avg audit"


   @lighthouse_staging
   @lighthouse
   @lighthouse_staging_logged_in_all
   Scenario: 16-lh all dashboard pages performance audit - GB Lighthouse logged in nonprod
    Given Logged in to "United Kingdom" customer account "lighthouseqa@mail.com" email and password "Password1234"
    Then Navigate to each dashboard page lighthouse "avg audit"

