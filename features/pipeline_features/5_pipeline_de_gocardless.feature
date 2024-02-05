@growth_regression
@pipeline_five
@pipe
Feature: scenario 5 for pipeline runs Go cardless

    #5. TestGermanSignupWithDirectDebit Gocardless-OpenBanking
    Scenario: 5 gocardless german dry food - pipeline GE signup
     Given on homepage and "Germany" country
     When Add "behave" information age "2" years neutered purebreed "Labrador Retriever" pipeline
     And Select gain weight motivation for dog food pipeline
     And Status no working dog weight "15" pipeline
     And Health Ingredients no issues international pipeline
     And Current diet select dry and wet food pipeline
     And Current food dry "Purina" selected wet "Kleine Dose (156g)" pipeline
     And Select flavour anything pipeline
     And Complete email page pipeline
     And select dry food only wet current diet pipeline in "Germany"
     And Select no treats Project Box
     And Pricing continue with gocardless pipeline
     And Checkout international address for Germany express delivery pipeline
     #Uncomment when openingbanking flow is enabled
     #And Checkout with OpenBanking
     And Checkout with gocardless account number "532013000" and bank card "37040044"
     Then Signup completed "Vielen Dank" displays




