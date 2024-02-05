@growth_regression
@nethl_ideal
Feature: iDEAL All Payment Options Signup
This feature needs to be ran on Staging due to external application requirements (MOLLIE integration), nightly runs points to staging.


#  https://tailscom.atlassian.net/browse/QA-930
  @netherlands_ideal_paid
  @nightly_chrome_four
  @roe
  Scenario: 901 dry food ideal paid - NE signup ideal
    Given on homepage and "Netherlands" country
     When Add "idealpaid" information age "2" years "5" months male neutered purebreed "Beagle"
     And Select gain weight motivation for dog food
     And Status no working dog weight "15"
     And Health Ingredients no issues
     And Current diet dry food international
     And Current food select no brand
     And Select flavour anything
     And Complete email page
     And select dry food only order while dry food only is in current diet in "Netherlands"
     And Select no treats Project Box
     And Pricing continue with ideal
     And Checkout international address for "Netherlands" future delivery date
     And Checkout with "Paid" ideal payment details
     Then Signup completed and dutch "Ga verder naar mijn dashboard" display

  @netherlands_ideal_open
  @nightly_chrome_fives
  @roe
  Scenario: 902 dry food ideal open - NE signup ideal
    Given on homepage and "Netherlands" country
    When Add "idealopen" information age "2" years "5" months male neutered purebreed "Beagle"
     And Select gain weight motivation for dog food
     And Status no working dog weight "15"
     And Health Ingredients no issues
     And Current diet dry food international
     And Current food select no brand
     And Select flavour anything
     And Complete email page
     And select dry food only order while dry food only is in current diet in "Netherlands"
     And Select no treats Project Box
     And Pricing continue with ideal
     And Checkout international address for "Netherlands" future delivery date
     And Checkout with "Open" ideal payment details
     Then Signup completed and dutch "Ga verder naar mijn dashboard" display

  @netherlands_ideal_failed
  @nightly_chrome_fives
  @roe
  Scenario: 903 dry food ideal failed - NE signup ideal
     Given on homepage and "Netherlands" country
      When Add "idealfailed" information age "2" years "5" months male neutered purebreed "Beagle"
     And Select gain weight motivation for dog food
     And Status no working dog weight "15"
     And Health Ingredients no issues
     And Current diet dry food international
     And Current food select no brand
     And Select flavour anything
     And Complete email page
     And select dry food only order while dry food only is in current diet in "Netherlands"
     And Select no treats Project Box
     And Pricing continue with ideal
     And Checkout international address for "Netherlands" future delivery date
     And Checkout with "Failed" ideal payment details
     Then Signup completed and dutch "Ga verder naar mijn dashboard" display

  @nightly_chrome_fives
  @netherlands_ideal_cancelled
  @roe
  Scenario: 904 dry food ideal cancelled - NE signup ideal
     Given on homepage and "Netherlands" country
     When Add "idealcancelled" information age "2" years "5" months male neutered purebreed "Beagle"
     And Select gain weight motivation for dog food
     And Status no working dog weight "15"
     And Health Ingredients no issues
     And Current diet dry food international
     And Current food select no brand
     And Select flavour anything
     And Complete email page
     And select dry food only order while dry food only is in current diet in "Netherlands"
     And Select no treats Project Box
     And Pricing continue with ideal
     And Checkout international address for "Netherlands" future delivery date
#     'Canceled' is purposely mispelled here due to Mollie having a typo in its application
     And Checkout with "Canceled" ideal payment details
     Then Signup completed and dutch "Ga verder naar mijn dashboard" display

  @nightly_chrome_six
  @netherlands_ideal_expired
  @roe
  Scenario: 905 dry food ideal expired - NE signup ideal
     Given on homepage and "Netherlands" country
      When Add "idealexpired" information age "2" years "5" months male neutered purebreed "Beagle"
     And Select gain weight motivation for dog food
     And Status no working dog weight "15"
     And Health Ingredients no issues
     And Current diet dry food international
     And Current food select no brand
     And Select flavour anything
     And Complete email page
     And select dry food only order while dry food only is in current diet in "Netherlands"
     And Select no treats Project Box
     And Pricing continue with ideal
     And Checkout international address for "Netherlands" future delivery date
     And Checkout with "Expired" ideal payment details
     Then Signup completed and dutch "Ga verder naar mijn dashboard" display