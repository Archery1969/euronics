Feature: Home Page Navigation and Actions

  Background: Accept cookies and enter postcode on the home page
    Given I am on the home page
    When I click the cookie accept button
    Then the cookie accept button should no longer be visible
    When I enter a postcode
    Then the postcode search input should no longer be visible

  Scenario: Search for a product by category, name, or SKU
    Given I am on the homepage
    When I search for a product by "category"
    Then I should see products related to the searched category

  Scenario: Navigate to my account page from header
    Given I am on the homepage
    When I click on the "my account" header link
    Then I should be taken to the login page

  Scenario: Navigate to store finder page from header
    Given I am on the homepage
    When I click on the "store finder" header link
    Then I should be taken to the store finder page

  Scenario: Navigate to shortlist page from header
    Given I am on the homepage
    When I click on the "shortlist" header link
    Then I should be taken to the shortlist page

  Scenario: Navigate to basket page from header
    Given I am on the homepage
    When I click on the "basket" header link
    Then I should be taken to the basket page

  Scenario: Navigate to About Us page from footer
    Given I am on the homepage
    When I click on the "about us" footer link
    Then I should see the About Us page

  Scenario: Navigate to Privacy Policy page from footer
    Given I am on the homepage
    When I click on the "privacy policy" footer link
    Then I should see the Privacy Policy page

  Scenario: Navigate to Cookie Policy page from footer
    Given I am on the homepage
    When I click on the "cookie policy" footer link
    Then I should see the Cookie Policy page

  Scenario: Navigate to Newsletter Sign-up page from footer
    Given I am on the homepage
    When I click on the "newsletter sign-up" footer link
    Then I should be taken to the newsletter sign-up page
