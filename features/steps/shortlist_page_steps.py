from behave import given, when, then
from playwright.sync_api import expect

from pages.shortlist_page import ShortlistPage


@given(u'I am on the shortlist page')
def step_impl(context):
    shortlist_page = ShortlistPage(context.page)
    expect(shortlist_page.page).to_have_title(shortlist_page.page_title())


@then(u'I should see the products added to the shortlist')
def step_impl(context):
    shortlist_page = ShortlistPage(context.page)
    expect(shortlist_page.product_list_locator()).to_be_visible()


@when(u'I remove the product from the shortlist')
def step_impl(context):
    shortlist_page = ShortlistPage(context.page)
    shortlist_page.remove_product_locator(action="click")


@when(u'I move the product from the shortlist to the basket')
def step_impl(context):
    shortlist_page = ShortlistPage(context.page)
    shortlist_page.move_to_basket_locator(action="click")


@then(u'The product should no longer be in the shortlist')
def step_impl(context):
    shortlist_page = ShortlistPage(context.page)
    expect(shortlist_page.product_list_locator()).not_to_be_visible()
