Feature: Registration Page Actions

  Background: Accept cookies and enter postcode on the home page
    Given I am on the home page
    When I click the cookie accept button
    Then the cookie accept button should no longer be visible
    When I enter a postcode
    Then the postcode search input should no longer be visible

  Scenario: Register a new user account
    Given I am on the registration page
    When I enter my title, first name, last name, email, and password
    And I confirm my password
    And I click the create account button
    Then my new account should be created successfully
