Feature: Product Page Actions

  Background: Accept cookies and enter postcode on the home page
    Given I am on the home page
    When I click the cookie accept button
    Then the cookie accept button should no longer be visible
    When I enter a postcode
    Then the postcode search input should no longer be visible

  Scenario: View product details
    Given I am on the product details page
    When I view the product details
    Then I should see the product name, description, image, price, and variants

  Scenario: Add product to shortlist
    Given I am on the product details page
    When I add the product to the shortlist
    Then the product should be added to the shortlist

  Scenario: Add product to basket
    Given I am on the product details page
    When I add the product to the basket
    Then the product should be added to the basket
