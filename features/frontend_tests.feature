Feature: Website Tests

  Background: Accept cookies and enter postcode on the home page
    Given I am on the home page
    When I click the cookie accept button
    Then the cookie accept button should no longer be visible
    When I enter a postcode
    Then the postcode search input should no longer be visible

  Scenario: User registration with valid data
    Given the user is on the registration page
    When the user enters valid registration details and submits the form
    Then the account is created successfully
    And the user is redirected to the login page
    And a welcome message is displayed on the login page

  Scenario: User registration with invalid data
    Given the user is on the registration page
    When the user enters invalid registration details and submits the form
    Then an error message is displayed for invalid fields
    And the user remains on the registration page

  Scenario: User login with valid credentials
    Given the user is on the login page
    When the user enters valid credentials
    Then the user is logged in successfully
    And the dashboard is displayed
    And the logout option is available

  Scenario: User login with invalid credentials
    Given the user is on the login page
    When the user enters invalid credentials
    Then an error message is displayed for invalid login
    And the user remains on the login page

  Scenario: User logout
    Given the user is logged in
    When the user clicks the logout button
    Then the user is logged out successfully
    And the homepage is displayed with a login option

  Scenario: Searching for a product
    Given the user is on the homepage
    When the user searches for a product using the search bar
    Then relevant products are displayed
    And each product includes its name, price, and image

  Scenario: Searching for a product with no results
    Given the user is on the homepage
    When the user searches for a non-existent product
    Then a "no products found" message is displayed

  Scenario: Applying filters to search results
    Given the user is viewing search results
    When the user applies a price filter
    Then the filtered results are displayed
    And the results match the price filter criteria

  Scenario: Clearing applied filters
    Given the user has applied filters
    When the user clears all filters
    Then all products are displayed in the search results
    And no filters are active

  Scenario: Viewing product details
    Given the user is on the search results page
    When the user clicks on a product
    Then the product details page is displayed
    And the product name, description, price, and options are shown

  Scenario: Selecting product options
    Given the user is on the product details page
    When the user selects an option like size or color
    Then the selected option is updated on the page
    And the "Add to cart" button becomes active

  Scenario: Adding a product to the cart
    Given the user is on the product details page
    When the user clicks "Add to cart"
    Then the product is added and cart icon reflects the items

  Scenario: Viewing the cart with products
    Given the user has products in the cart
    When the user views the cart
    Then the cart displays all items with their quantity, price, and total
    And the cart subtotal is displayed correctly

  Scenario: Updating product quantity in the cart
    Given the user is viewing the cart
    When the user increases the quantity of a product
    Then the cart total updates accordingly
    And the correct quantity is reflected in the cart

  Scenario: Removing a product from the cart
    Given the user is viewing the cart
    When the user removes a product
    Then the product is removed and total updates
    And a message confirming the product removal is displayed

  Scenario: Guest user checkout with payment
    Given the user has products in the cart
    And the user proceeds to checkout
    When the user enters valid shipping information
    And the user selects a payment method
    And the user enters valid payment details
    And the user confirms the payment
    Then the order is placed successfully
    And the order confirmation page is displayed

  Scenario: Registered user checkout with saved address
    Given the user is logged in
    And the user has added products to the cart
    When the user proceeds to checkout
    Then the saved shipping information is pre-filled
    And the user selects a payment method
    And the user enters valid payment details
    When the user confirms the payment
    Then the order is placed successfully
    And the order confirmation page is displayed

  Scenario: Viewing order history
    Given the user is logged in
    When the user navigates to the "Order History" page
    Then all past orders are listed
    And each order shows the order number, status, and total amount

  Scenario: Applying a valid coupon code
    Given the user has products in the cart
    When the user applies a valid coupon code
    Then the discount is applied to the total price
    And the discount amount is shown in the cart summary

  Scenario: Entering an invalid coupon code
    Given the user is in checkout
    When the user applies an invalid or expired coupon code
    Then an error message is displayed
    And no discount is applied to the total price
