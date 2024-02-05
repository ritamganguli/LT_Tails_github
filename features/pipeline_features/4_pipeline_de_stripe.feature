@growth_regression
@pipeline_four
@pipe
Feature: pipeline signup - 4 dry food stripe - german box flow

 #	4. TestGermanSignup Stripe
  Scenario: 4 german dry food stripe - pipeline GE signup
     Given on homepage and "Germany" country
     When Add "behave" information age "2" years neutered purebreed "Labrador Retriever" pipeline
     And Select gain weight motivation for dog food pipeline
     And Status no working dog weight "15" pipeline
     And Health Ingredients no issues international pipeline
     And Current diet select dry and wet food pipeline
     And Current food dry "Purina" selected wet "Mini can (156g)" pipeline
     And Select flavour anything pipeline
     And Complete email page pipeline
     And select dry food only wet current diet pipeline in "Germany"
     And Select no treats Project Box
     And Pricing continue with card pipeline
     And Checkout international address for Germany express delivery pipeline
     And Checkout with stripe payment details pipeline DE
    Then Signup completed and german "Weiter zu meinem Dashboard" display pipeline


