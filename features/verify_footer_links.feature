Feature: Verify Footer Links

  Background: Accept cookies and enter postcode on the home page
    Given I am on the home page
    And the cookie accept button is visible
    When I click the cookie accept button
    Then the cookie accept button should no longer be visible
    And the postcode input should be visible
    When I enter a postcode
    And I click the search button
    Then the postcode input should no longer be visible

  Scenario: Verify Contact Us link
    Given I am on the home page
    When I click the Contact Us link
    Then I should be navigated to the Contact Us page

  Scenario: Verify FAQ link
    Given I am on the home page
    When I click the FAQ link
    Then I should be navigated to the FAQ page

  Scenario: Verify Delivery & Installation link
    Given I am on the home page
    When I click the Delivery & Installation link
    Then I should be navigated to the Delivery & Installation page
