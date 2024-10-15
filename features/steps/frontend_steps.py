from behave import given, when, then

from pages.home_page import HomePage
from utils.helper import *


@given(u'I am on the home page')
def step_impl(context):
    home_page = HomePage(context.page)
    expect(home_page.page).to_have_title(home_page.page_title())


@when(u'I click the cookie accept button')
def step_impl(context):
    home_page = HomePage(context.page)
    home_page.cookie_button_locator(action="click")


@then(u'the cookie accept button should no longer be visible')
def step_impl(context):
    home_page = HomePage(context.page)
    expect(home_page.cookie_button_locator()).to_be_hidden()


@when(u'I enter a postcode')
def step_impl(context):
    home_page = HomePage(context.page)
    home_page.postcode_input_locator(action="fill", fill_value=context.config.userdata.get("storefront_postcode"))
    home_page.postcode_search_locator(action="click")


@then(u'the postcode search input should no longer be visible')
def step_impl(context):
    home_page = HomePage(context.page)
    expect(home_page.postcode_input_locator()).to_be_hidden()


@given(u'the user is on the registration page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user is on the registration page')


@when(u'the user enters valid registration details and submits the form')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user enters valid registration details and submits the form')


@then(u'the account is created successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the account is created successfully')


@then(u'the user is redirected to the login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user is redirected to the login page')


@then(u'a welcome message is displayed on the login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a welcome message is displayed on the login page')


@when(u'the user enters invalid registration details and submits the form')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user enters invalid registration details and submits the form')


@then(u'an error message is displayed for invalid fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then an error message is displayed for invalid fields')


@then(u'the user remains on the registration page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user remains on the registration page')


@given(u'the user is on the login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user is on the login page')


@when(u'the user enters valid credentials')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user enters valid credentials')


@then(u'the user is logged in successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user is logged in successfully')


@then(u'the dashboard is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the dashboard is displayed')


@then(u'the logout option is available')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the logout option is available')


@when(u'the user enters invalid credentials')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user enters invalid credentials')


@then(u'an error message is displayed for invalid login')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then an error message is displayed for invalid login')


@then(u'the user remains on the login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user remains on the login page')


@given(u'the user is logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user is logged in')


@when(u'the user clicks the logout button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user clicks the logout button')


@then(u'the user is logged out successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user is logged out successfully')


@then(u'the homepage is displayed with a login option')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the homepage is displayed with a login option')


@given(u'the user is on the homepage')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user is on the homepage')


@when(u'the user searches for a product using the search bar')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user searches for a product using the search bar')


@then(u'relevant products are displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then relevant products are displayed')


@then(u'each product includes its name, price, and image')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then each product includes its name, price, and image')


@when(u'the user searches for a non-existent product')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user searches for a non-existent product')


@then(u'a "no products found" message is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a "no products found" message is displayed')


@given(u'the user is viewing search results')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user is viewing search results')


@when(u'the user applies a price filter')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user applies a price filter')


@then(u'the filtered results are displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the filtered results are displayed')


@then(u'the results match the price filter criteria')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the results match the price filter criteria')


@given(u'the user has applied filters')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user has applied filters')


@when(u'the user clears all filters')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user clears all filters')


@then(u'all products are displayed in the search results')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then all products are displayed in the search results')


@then(u'no filters are active')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then no filters are active')


@given(u'the user is on the search results page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user is on the search results page')


@when(u'the user clicks on a product')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user clicks on a product')


@then(u'the product details page is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the product details page is displayed')


@then(u'the product name, description, price, and options are shown')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the product name, description, price, and options are shown')


@given(u'the user is on the product details page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user is on the product details page')


@when(u'the user selects an option like size or color')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user selects an option like size or color')


@then(u'the selected option is updated on the page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the selected option is updated on the page')


@then(u'the "Add to cart" button becomes active')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the "Add to cart" button becomes active')


@when(u'the user clicks "Add to cart"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user clicks "Add to cart"')


@then(u'the product is added and cart icon reflects the items')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the product is added and cart icon reflects the items')


@given(u'the user has products in the cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user has products in the cart')


@when(u'the user views the cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user views the cart')


@then(u'the cart displays all items with their quantity, price, and total')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the cart displays all items with their quantity, price, and total')


@then(u'the cart subtotal is displayed correctly')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the cart subtotal is displayed correctly')


@given(u'the user is viewing the cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user is viewing the cart')


@when(u'the user increases the quantity of a product')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user increases the quantity of a product')


@then(u'the cart total updates accordingly')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the cart total updates accordingly')


@then(u'the correct quantity is reflected in the cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the correct quantity is reflected in the cart')


@when(u'the user removes a product')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user removes a product')


@then(u'the product is removed and total updates')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the product is removed and total updates')


@then(u'a message confirming the product removal is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a message confirming the product removal is displayed')


@given(u'the user proceeds to checkout')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user proceeds to checkout')


@when(u'the user enters valid shipping information')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user enters valid shipping information')


@when(u'the user selects a payment method')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user selects a payment method')


@when(u'the user enters valid payment details')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user enters valid payment details')


@when(u'the user confirms the payment')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user confirms the payment')


@then(u'the order is placed successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the order is placed successfully')


@then(u'the order confirmation page is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the order confirmation page is displayed')


@given(u'the user has added products to the cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user has added products to the cart')


@when(u'the user proceeds to checkout')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user proceeds to checkout')


@then(u'the saved shipping information is pre-filled')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the saved shipping information is pre-filled')


@then(u'the user selects a payment method')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user selects a payment method')


@then(u'the user enters valid payment details')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user enters valid payment details')


@when(u'the user navigates to the "Order History" page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user navigates to the "Order History" page')


@then(u'all past orders are listed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then all past orders are listed')


@then(u'each order shows the order number, status, and total amount')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then each order shows the order number, status, and total amount')


@when(u'the user applies a valid coupon code')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user applies a valid coupon code')


@then(u'the discount is applied to the total price')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the discount is applied to the total price')


@then(u'the discount amount is shown in the cart summary')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the discount amount is shown in the cart summary')


@given(u'the user is in checkout')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user is in checkout')


@when(u'the user applies an invalid or expired coupon code')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user applies an invalid or expired coupon code')


@then(u'an error message is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then an error message is displayed')


@then(u'no discount is applied to the total price')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then no discount is applied to the total price')
