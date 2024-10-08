Feature: Verify Header Links

  Scenario: Accept cookies and enter postcode on the home page
    Given I am on the home page
    When I click the cookie accept button
    Then the cookie accept button should be hidden
    And I see the postcode input
    When I enter a postcode
    And I click the search button
    Then the postcode input should be hidden
