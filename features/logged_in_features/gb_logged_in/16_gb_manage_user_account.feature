@owner_regression
@owner
Feature: UK - Manage user account

  @nightly_iphone_two
  @uksmoke_login
  Scenario: 6001 User account login from menu - UK logged in
  Given Logged in to "United Kingdom" customer account "active" and store "1"
  Then customer lands on dashboard

  @nightly_iphone_one
  @uksmoke_forgotpassword
  Scenario: 6002 User account forgot password - UK logged in
  Given Attempted password recovery of "United Kingdom" customer account "2" and store "1"
  Then confirm password reset email is sent
  Then email exists in frontyard

  @nightly_iphone_one
  @logout_user
  Scenario: 6003 User account Log out user session from dashboard page - UK logged in
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    When Select log out
    Then Confirm logout message "You are logged out." displays

  @nightly_iphone_four
  @update_passw
  Scenario: 6004 User account update password - UK logged in
    Given Logged in to "United Kingdom" customer account "active" and store "1"
    When Select Account page and confirm "Account settings" displays
    And Select update password
    And Add current and new password
    Then Confirm account page "Your password has been updated" displays

