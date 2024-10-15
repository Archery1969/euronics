from behave import given, when, then
from playwright.sync_api import expect

from pages.basket_page import BasketPage


@given(u'I am on the basket page')
def step_impl(context):
    basket_page = BasketPage(context.page)
    expect(basket_page.page).to_have_title(basket_page.page_title())


@then(u'I should see the product name, description, price, and quantity')
def step_impl(context):
    basket_page = BasketPage(context.page)
    expect(basket_page.product_name_locator()).to_be_visible()
    expect(basket_page.product_description_locator()).to_be_visible()
    expect(basket_page.product_price_locator()).to_be_visible()
    expect(basket_page.product_quantity_locator()).to_be_visible()


@when(u'I increase the product quantity')
def step_impl(context):
    basket_page = BasketPage(context.page)
    basket_page.increase_quantity_locator(action="click")


@when(u'I decrease the product quantity')
def step_impl(context):
    basket_page = BasketPage(context.page)
    basket_page.decrease_quantity_locator(action="click")


@when(u'I remove the product from the basket')
def step_impl(context):
    basket_page = BasketPage(context.page)
    basket_page.remove_product_locator(action="click")


@when(u'I proceed to checkout')
def step_impl(context):
    basket_page = BasketPage(context.page)
    basket_page.proceed_to_checkout_locator(action="click")


@then(u'The product quantity should be updated')
def step_impl(context):
    basket_page = BasketPage(context.page)
    expect(basket_page.product_quantity_locator()).to_have_value("Updated Quantity")


@then(u'The product should be removed')
def step_impl(context):
    basket_page = BasketPage(context.page)
    expect(basket_page.product_name_locator()).not_to_be_visible()


@then(u'I should be taken to the checkout page')
def step_impl(context):
    basket_page = BasketPage(context.page)
    expect(basket_page.checkout_page_locator()).to_be_visible()
