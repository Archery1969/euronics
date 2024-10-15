Feature: Account Page Actions

  Background: Accept cookies and enter postcode on the home page
    Given I am on the home page
    When I click the cookie accept button
    Then the cookie accept button should no longer be visible
    When I enter a postcode
    Then the postcode search input should no longer be visible

  Scenario: View order history
    Given I am on the account page
    When I view my order history
    Then I should see my previous orders

  Scenario: Update user details
    Given I am on the account page
    When I update my user details
    Then my details should be saved successfully

  Scenario: View and update address book
    Given I am on the account page
    When I view my address book
    And I update my address
    Then the updated address should be saved
