from behave import given, when, then
from playwright.sync_api import expect

from pages.product_page import ProductPage


@given(u'I am on the product details page')
def step_impl(context):
    product_page = ProductPage(context.page)
    expect(product_page.page).to_have_title(product_page.page_title())


@when(u'I view the product details')
def step_impl(context):
    product_page = ProductPage(context.page)
    expect(product_page.product_name_locator()).to_be_visible()
    expect(product_page.product_description_locator()).to_be_visible()
    expect(product_page.product_image_locator()).to_be_visible()
    expect(product_page.product_price_locator()).to_be_visible()
    expect(product_page.product_variants_locator()).to_be_visible()


@when(u'I add the product to the shortlist')
def step_impl(context):
    product_page = ProductPage(context.page)
    product_page.add_to_shortlist_locator(action="click")


@when(u'I add the product to the basket')
def step_impl(context):
    product_page = ProductPage(context.page)
    product_page.add_to_basket_locator(action="click")


@then(u'The product should be added to the shortlist')
def step_impl(context):
    product_page = ProductPage(context.page)
    expect(product_page.shortlist_confirmation_locator()).to_be_visible()


@then(u'The product should be added to the basket')
def step_impl(context):
    product_page = ProductPage(context.page)
    expect(product_page.basket_confirmation_locator()).to_be_visible()
