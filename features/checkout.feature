Feature: Checkout Tests

  Background: Accept cookies and enter postcode on the home page
    Given I am on the home page
    When I click the cookie accept button
    Then the cookie accept button should no longer be visible
    When I enter a postcode
    Then the postcode search input should no longer be visible

  Scenario: Guest Checkout using Debit Card
    Given I am on the homepage
    When I search for a product by name or category
    And I select a product from the search results
    And I view the product details page
    And I add the product to my cart
    And I view my shopping cart
    And I proceed to checkout as a guest
    And I enter my personal information (name, email, phone)
    And I enter my delivery address
    And I choose Debit Card as the payment method
    And I enter valid Debit Card details
    And I review my order summary
    And I place the order
    Then I should be redirected to the order confirmation page

  Scenario: Guest Checkout using Credit Card
    Given I am on the homepage
    When I search for a product by name or category
    And I select a product from the search results
    And I view the product details page
    And I add the product to my cart
    And I view my shopping cart
    And I proceed to checkout as a guest
    And I enter my personal information (name, email, phone)
    And I enter my delivery address
    And I choose Credit Card as the payment method
    And I enter valid Credit Card details
    And I review my order summary
    And I place the order
    Then I should be redirected to the order confirmation page

  Scenario: Guest Checkout using PayPal
    Given I am on the homepage
    When I search for a product by name or category
    And I select a product from the search results
    And I view the product details page
    And I add the product to my cart
    And I view my shopping cart
    And I proceed to checkout as a guest
    And I enter my personal information (name, email, phone)
    And I enter my delivery address
    And I choose PayPal as the payment method
    And I enter valid PayPal details
    And I review my order summary
    And I place the order
    Then I should be redirected to the order confirmation page

  Scenario: Guest Checkout using Finance
    Given I am on the homepage
    When I search for a product by name or category
    And I select a product from the search results
    And I view the product details page
    And I add the product to my cart
    And I view my shopping cart
    And I proceed to checkout as a guest
    And I enter my personal information (name, email, phone)
    And I enter my delivery address
    And I choose Finance as the payment method
    And I enter valid Finance details
    And I review my order summary
    And I place the order
    Then I should be redirected to the order confirmation page
