@lighthouse_prod_feature
@lighthouse
Feature: Prod UK Signup and logged in lighthouse reporting

    For all the collected audit metrics in this lighhouse test feature the thresholds are set as follows: First Contentful Paint (FCP) = 7s, Largest Contentful Paint(LCP) = 7s,
    Speed Index (SI) = 5.8 category, Performance 100 %

   @lighthouse_prod_signup
   Scenario: 01-lh PROD dry wet and treats stripe flow - GB Lighthouse signup prod
     Given on homepage for prod box
     When navigate into signup flow in "United Kingdom" country prod lighthouse "none"
     And Add "lighthouse" information age "2" year neutered purebreed "Labrador Retriever" lighthouse "avg audit"
     And Select gain weight motivation for dog food lighthouse "avg audit"
     And Status no working dog weight "15" lighthouse "avg audit"
     And Health Ingredients no issues lighthouse "avg audit"
     And Current diet select dry wet food and treats other food lighthouse "avg audit"
     And lighthouse current food dry "Purina" selected wet "Mini can (156g)" lighthouse "avg audit"
     And Select flavour anything lighthouse "avg audit"
     And Complete email page for prod lighthouse "avg audit"
     And performance select dry and wet Project Box lighthouse "avg audit"
     And Select no treats Project Box lighthouse "avg audit"
     And Pricing continue with card lighthouse "avg audit"
     And Checkout address postcode "TW9 1BN" express delivery date prod lighthouse "avg audit"


   @lighthouse_prod
   @lighthouse_breed_prod
   Scenario: 02-lh PROD mydog and breed avg audit load GB Lighthouse signup prod
   Given on homepage for prod box
   When navigate into signup flow in "United Kingdom" country prod lighthouse "none"
   When Add "lighthouse" information age "2" year neutered purebreed "Labrador Retriever" lighthouse "avg audit"

   @lighthouse_prod
   @lighthouse_motivation_prod
   Scenario: 03-lh PROD motivation avg audit load - GB Lighthouse signup prod
      Given on homepage for prod box
      When navigate into signup flow in "United Kingdom" country prod lighthouse "none"
      When Add "lighthouse" information age "2" year neutered purebreed "Labrador Retriever" lighthouse "none"
      And Select gain weight motivation for dog food lighthouse "avg audit"

   @lighthouse_prod
   @lighthouse_weight_prod
   Scenario: 04-lh PROD weight activity avg audit load - GB Lighthouse signup prod
      Given on homepage for prod box
      When navigate into signup flow in "United Kingdom" country prod lighthouse "none"
      And Add "lighthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15" lighthouse "avg audit"

   @lighthouse_prod
   @lighthouse_health_prod
   Scenario: 05-lh PROD health avg audit load - GB Lighthouse signup prod
      Given on homepage for prod box
      When navigate into signup flow in "United Kingdom" country prod lighthouse "none"
      And Add "lighthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
       And Health Ingredients no issues lighthouse "avg audit"

   @lighthouse_prod
   @lighthouse_box_dry_prod
   Scenario: 06-lh PROD dry wet avg audit load - GB Lighthouse signup prod
      Given on homepage for prod box
      When navigate into signup flow in "United Kingdom" country prod lighthouse "none"
      And Add "lighthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
       And Health Ingredients no issues
       And Current diet select dry wet food and treats other food lighthouse "avg audit"

   @lighthouse_prod
   @lighthouse_food_prod
   Scenario: 07-lh PROD current diet avg audit load - GB Lighthouse signup prod
      Given on homepage for prod box
      When navigate into signup flow in "United Kingdom" country prod lighthouse "none"
      And Add "lighthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
       And Health Ingredients no issues
       And Current diet select dry wet food and treats other food lighthouse "avg audit"

   @lighthouse_prod
   @lighthouse_current_food_prod
   Scenario: 08-lh PROD current food avg audit load - GB Lighthouse signup prod
      Given on homepage for prod box
      When navigate into signup flow in "United Kingdom" country prod lighthouse "none"
      And Add "lighthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
      And Health Ingredients no issues
      And Current diet select dry wet food and treats other food
      And Performance current food dry "Purina" selected wet "Mini can (156g)" lighthouse "avg audit" prod

   @lighthouse_prod
   @lighthouse_flavour_prod
   Scenario: 09-lh PROD current flavour avg audit load - GB Lighthouse signup prod
      Given on homepage for prod box
      When navigate into signup flow in "United Kingdom" country prod lighthouse "none"
      And Add "lighthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
      And Health Ingredients no issues
      And Current diet select dry wet food and treats other food
      And lighthouse current food dry "Purina" selected wet "Mini can (156g)" lighthouse "none"
      And Select flavour anything lighthouse "avg audit"

   @lighthouse_prod
   @lighthouse_email_prod
   Scenario: 10-lh PROD email avg audit load - GB Lighthouse signup prod
      Given on homepage for prod box
      When navigate into signup flow in "United Kingdom" country prod lighthouse "none"
      And Add "lighthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
      And Health Ingredients no issues
      And Current diet select dry wet food and treats other food
      And lighthouse current food dry "Purina" selected wet "Mini can (156g)" lighthouse "none"
      And Select flavour anything
      And Complete email page for prod lighthouse "avg audit"

   @lighthouse_prod
   @lighthouse_box_prod
   Scenario: 11-lh PROD dry wet avg audit load - GB Lighthouse signup prod
      Given on homepage for prod box
      When navigate into signup flow in "United Kingdom" country prod lighthouse "none"
      And Add "lighthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
      And Health Ingredients no issues
      And Current diet select dry wet food and treats other food
      And lighthouse current food dry "Purina" selected wet "Mini can (156g)" lighthouse "none"
      And Select flavour anything
      And Complete email page for prod lighthouse "none"
      And performance select dry and wet Project Box lighthouse "avg audit"


   @lighthouse_prod
   @lighthouse_box_treat_prod
   Scenario: 12-lh PROD treats avg audit load - GB Lighthouse signup prod
      Given on homepage for prod box
      When navigate into signup flow in "United Kingdom" country prod lighthouse "none"
      And Add "lighthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
      And Health Ingredients no issues
      And Current diet select dry wet food and treats other food
      And lighthouse current food dry "Purina" selected wet "Mini can (156g)" lighthouse "none"
      And Select flavour anything
      And Complete email page for prod lighthouse "none"
      And select dry and wet Project Box in "United Kingdom"
      And Select no treats Project Box lighthouse "avg audit"

   @lighthouse_prod
   @lighthouse_pricing_prod
   Scenario: 13-lh PROD pricing avg audit load - GB Lighthouse signup prod
      Given on homepage for prod box
      When navigate into signup flow in "United Kingdom" country prod lighthouse "none"
      And Add "lighthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
      And Health Ingredients no issues
      And Current diet select dry wet food and treats other food
      And lighthouse current food dry "Purina" selected wet "Mini can (156g)" lighthouse "none"
      And Select flavour anything
      And Complete email page for prod lighthouse "none"
      And select dry and wet Project Box in "United Kingdom"
      And Select no treats Project Box
       And Pricing continue with card lighthouse "avg audit"

   @lighthouse_prod
   @lighthouse_checkout_prod
   Scenario: 14-lh PROD checkout avg audit load - GB Lighthouse signup prod
      Given on homepage for prod box
      When navigate into signup flow in "United Kingdom" country prod lighthouse "none"
      And Add "lighthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
      And Health Ingredients no issues
      And Current diet select dry wet food and treats other food
      And lighthouse current food dry "Purina" selected wet "Mini can (156g)" lighthouse "none"
      And Select flavour anything
      And Complete email page for prod lighthouse "none"
      And select dry and wet Project Box in "United Kingdom"
      And Select no treats Project Box
      And Pricing continue with card
      And Checkout address postcode "TW9 1BN" express delivery date prod lighthouse "avg audit"

   @lighthouse_prod
   @lighthouse_stripe_prod
   Scenario: 15-lh PROD stripe avg audit load - GB Lighthouse signup prod
      Given on homepage for prod box
      When navigate into signup flow in "United Kingdom" country prod lighthouse "none"
      And Add "lighthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
      And Health Ingredients no issues
      And Current diet select dry wet food and treats other food
      And lighthouse current food dry "Purina" selected wet "Mini can (156g)" lighthouse "none"
      And Select flavour anything
      And Complete email page for prod lighthouse "none"
      And select dry and wet Project Box in "United Kingdom"
      And Select no treats Project Box
      And Pricing continue with card
      And Checkout address postcode "TW9 1BN" express delivery date prod lighthouse "none"
      And Checkout with stripe payment details lighthouse "avg audit"


   @lighthouse_prod
   @lighthouse_sign_complete_prod
   Scenario: 16-lh PROD avg audit load - GB Lighthouse signup prod
      Given on homepage for prod box
      When navigate into signup flow in "United Kingdom" country prod lighthouse "none"
      And Add "lighthouse" information age "2" years neutered purebreed "Labrador Retriever"
      And Select gain weight motivation for dog food
      And Status no working dog weight "15"
      And Health Ingredients no issues
      And Current diet select dry wet food and treats other food
      And lighthouse current food dry "Purina" selected wet "Mini can (156g)" lighthouse "none"
      And Select flavour anything
      And Complete email page for prod lighthouse "none"
      And select dry and wet Project Box in "United Kingdom"
      And Select no treats Project Box
      And Pricing continue with card
      And Checkout address postcode "TW9 1BN" express delivery date prod lighthouse "none"
     Then Checkout with stripe payment details prod lighthouse "avg audit"


  @lighthouse_prod @lighthouse @lighthouse_dashboard_pages_prod
  Scenario: 17-lh PROD all dashboard pages Treatment, Feeding plan, Refer a friend, Account, Profile, Shop - GB Lighthouse logged in prod
     Given Logged in to PROD "United Kingdom" customer account "lighthouse@mail.com" and password "Password1234" lighthouse
     Then Navigate to each dashboard page lighthouse "avg audit"