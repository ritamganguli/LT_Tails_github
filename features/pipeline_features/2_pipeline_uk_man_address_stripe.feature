@growth_regression
@pipeline_two
@pipe
Feature: pipeline signup - 2 stripe manual address pipeline

#   2. TestBritishSignupManualAddressCardNoBilling
   Scenario: 2 stripe manual address - pipeline UK signup
     Given on homepage and "United Kingdom" country pipeline
     When Add "behave" information age "2" years neutered purebreed "Labrador Retriever" pipeline
     And Select gain weight motivation for dog food pipeline
     And Status no working dog weight "15" pipeline
     And Health Ingredients no issues pipeline
     And Current diet select dry and wet food pipeline
     And Current food dry "Purina" selected wet "Mini can (156g)" pipeline
     And Select flavour anything pipeline
     And Complete email page pipeline
     And select dry and wet Project Box in "United Kingdom"
     And Select no treats Project Box
     And Pricing continue with card pipeline
     And Checkout manual address "7 Kew Foot Road" and "London" "TW92SS" express delivery date pipeline
     And Checkout with stripe payment details pipeline
     Then Signup completed and "Continue to my dashboard" display pipeline
