Feature: npd tests - signup - all markets
  # Testing the signup flow for new products - not to be included in nightly run


  Scenario: 100001 - new signup GB - add NPD product
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
     And Add "Superfood Lamb Bites" Project Box and claim "Hypoallergenic and grain-free recipe"
     Then Confirm "Superfood Lamb Bites" displayed in price table


  Scenario: 100002 - new signup FR - add NPD product
    Given on homepage and "France" country
     When Add "behave" information age "2" years neutered purebreed "Labrador Retriever" pipeline
     And Select gain weight motivation for dog food pipeline
     And Status no working dog weight "15" pipeline
     And Health Ingredients no issues international pipeline
     And Current diet select dry and wet food pipeline
     And Current food dry "Purina" selected wet "Mini can (156g)" pipeline
     And Select flavour anything pipeline
     And Complete email page pipeline
     And select dry and wet Project Box FR
     And Add "Poo bags" Project Box and claim "Faits avec 100% de matériaux recyclés"
     Then Confirm "Sacs à crottes" displayed in price table


   Scenario: 100003 - new signup DE - add NPD product
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
     And Add "Poo bags" Project Box and claim "Aus 100% recycelten Materialien"
     Then Confirm "Kotbeutel" displayed in price table

  Scenario: 100004 - new signup DE - product not shown
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
     Then Confirm "Superfood lamb" not shown