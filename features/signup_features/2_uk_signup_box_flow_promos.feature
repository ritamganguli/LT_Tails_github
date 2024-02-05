@growth_regression
@uk_stripe_promo
Feature: UK signup flow box with promos

   @uk_stripe_raf_promo
   @nightly_chrome_six
   Scenario: 00100 dry food stripe RAF promo - UK signup
     Given on homepage and "United Kingdom" country pb
     When Add promo "MILENFD7"
     And Add "dogone" information age "2" years "5" months male neutered unknownbreed "Giant"
     And Select gain weight motivation for dog food
     And Status no working dog weight estimate
     And Health Ingredients no issues UK
     And Current diet dry food
     And Current food select no brand
     And Select flavour anything
     And Complete email page
     And select dry food only Project Box
     And Select no treats Project Box
     And Pricing continue with card
     And Checkout address postcode "TW92SS" future delivery date
     And Checkout with stripe payment details
     Then Signup completed and "Continue to my dashboard" display


  @uk_remote_ppc_promo
  @nightly_android_two
  Scenario: 00300 dry & wet food - isle postcode no express - PPC Health campaign promo - UK signup
     Given on homepage and "United Kingdom" country pb
     When Add promo "JUR4SR"
     And Add "dogone" information age "2" years "5" months male neutered purebreed "Beagle"
     And Select gain weight motivation for dog food
     And Status no working dog weight "15"
     And Health Ingredients no issues UK
     And Current diet select dry and wet food
     And Current food no dry selected wet "Mini can (156g)"
     And Select flavour anything
     And Complete email page
     And select dry and wet Project Box in "United Kingdom"
     And Select no treats Project Box
     And Pricing continue with card
     Then Checkout with remote postcode "PH106LP"


  @uk_stripe_incomplete_promo
  @nightly_chrome_five
  Scenario: 00400 dry food stripe incompletes promo - UK signup
     Given on homepage and "United Kingdom" country pb
     When Add promo "Y9FGWU"
     And Add "dogone" information age "2" years "5" months male neutered unknownbreed "Giant"
     And Select gain weight motivation for dog food
     And Status no working dog weight estimate
     And Health Ingredients no issues UK
     And Current diet dry food
     And Current food select no brand
     And Select flavour anything
     And Complete email page
     And select dry food only Project Box
     And Select no treats Project Box
     And Pricing continue with card
     And Checkout address postcode "TW92SS" future delivery date
     And Checkout with stripe payment details
     Then Signup completed and "Continue to my dashboard" display
