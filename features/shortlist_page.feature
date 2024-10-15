Feature: Shortlist Page Actions

  Background: Accept cookies and enter postcode on the home page
    Given I am on the home page
    When I click the cookie accept button
    Then the cookie accept button should no longer be visible
    When I enter a postcode
    Then the postcode search input should no longer be visible

  Scenario: View products in shortlist
    Given I am on the shortlist page
    Then I should see the products added to the shortlist

  Scenario: Remove product from shortlist
    Given I am on the shortlist page
    When I remove the product from the shortlist
    Then the product should no longer be in the shortlist

  Scenario: Move product from shortlist to basket
    Given I am on the shortlist page
    When I move the product from the shortlist to the basket
    Then the product should be added to the basket
