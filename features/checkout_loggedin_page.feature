Feature: Logged-In User Checkout

  Background: Accept cookies and enter postcode on the home page
    Given I am on the home page
    When I click the cookie accept button
    Then the cookie accept button should no longer be visible
    When I enter a postcode
    Then the postcode search input should no longer be visible

  Scenario: Login to account and proceed with checkout
    Given I am on the login page
    When I log in with my email and password
    And I proceed to checkout
    Then I should be on the checkout page

  Scenario: Enter delivery address and select date
    Given I am on the checkout page as a logged-in user
    When I select my saved delivery address
    And I select a delivery date
    Then the delivery details should be saved

  Scenario: Select payment method and place order
    Given I am on the checkout page as a logged-in user
    When I select "Credit Card" as the payment method
    And I enter my payment details
    And I place the order
    Then I should be taken to the order confirmation page
