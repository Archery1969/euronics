Feature: Basket Page Actions

  Background: Accept cookies and enter postcode on the home page
    Given I am on the home page
    When I click the cookie accept button
    Then the cookie accept button should no longer be visible
    When I enter a postcode
    Then the postcode search input should no longer be visible

  Scenario: View basket contents
    Given I am on the basket page
    Then I should see the product name, description, price, and quantity

  Scenario: Increase product quantity
    Given I am on the basket page
    When I increase the product quantity
    Then the product quantity should be updated

  Scenario: Decrease product quantity
    Given I am on the basket page
    When I decrease the product quantity
    Then the product quantity should be updated

  Scenario: Remove product from basket
    Given I am on the basket page
    When I remove the product from the basket
    Then the product should be removed

  Scenario: Proceed to checkout
    Given I am on the basket page
    When I proceed to checkout
    Then I should be taken to the checkout page
