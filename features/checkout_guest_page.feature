Feature: Guest User Checkout

  Background: Accept cookies and enter postcode on the home page
    Given I am on the home page
    When I click the cookie accept button
    Then the cookie accept button should no longer be visible
    When I enter a postcode
    Then the postcode search input should no longer be visible

  Scenario: Enter personal information
    Given I am on the checkout page as a guest
    When I enter my personal information
    Then my personal information should be saved

  Scenario: Enter delivery address
    Given I am on the checkout page as a guest
    When I enter my delivery address
    Then my delivery address should be saved

  Scenario: Select delivery date
    Given I am on the checkout page as a guest
    When I select a delivery date
    Then the delivery date should be updated

  Scenario: Select payment method and place order
    Given I am on the checkout page as a guest
    When I select "Debit Card" as the payment method
    And I enter my payment details
    And I place the order
    Then I should be taken to the order confirmation page
