Feature: Verify Header Links

  Scenario: Accept cookies and enter postcode on the home page
    Given I am on the home page
    And the cookie accept button is visible
    When I click the cookie accept button
    Then the cookie accept button should no longer be visible
    And the postcode input should be visible
    When I enter a postcode
    And I click the search button
    Then the postcode input should no longer be visible
