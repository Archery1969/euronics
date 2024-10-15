Feature: Login Page Actions

  Background: Accept cookies and enter postcode on the home page
    Given I am on the home page
    When I click the cookie accept button
    Then the cookie accept button should no longer be visible
    When I enter a postcode
    Then the postcode search input should no longer be visible

  Scenario: Enter login credentials
    Given I am on the login page
    When I enter my email and password
    And I click the login button
    Then I should be logged in successfully

  Scenario: Click the forgot password link
    Given I am on the login page
    When I click the forgot password link
    Then I should be taken to the password reset page
