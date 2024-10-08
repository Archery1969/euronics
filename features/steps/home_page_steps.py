from behave import given, when, then

from utils.helper import *


@given(u'I am on the home page')
def step_impl(context):
    page: Page = context.page
    expect(page).to_have_title(home_page_locators(page).home_page_title)


@when(u'I click the cookie accept button')
def step_impl(context):
    page: Page = context.page
    home_page_locators(page).cookie_accept_button.click(timeout=global_timeout)


@then(u'the cookie accept button should be hidden')
def step_impl(context):
    page: Page = context.page
    expect(home_page_locators(page).cookie_accept_button).to_be_hidden()


@then(u'the postcode input should be visible')
def step_impl(context):
    page: Page = context.page
    expect(home_page_locators(page).postcode_input).to_be_visible()


@when(u'I enter a postcode')
def step_impl(context):
    page: Page = context.page
    home_page_locators(page).postcode_input.fill("BN10 7PU")


@when(u'I click the search button')
def step_impl(context):
    page: Page = context.page
    home_page_locators(page).postcode_search_button.click(timeout=global_timeout)


@then(u'the postcode input should be hidden')
def step_impl(context):
    page: Page = context.page
    expect(home_page_locators(page).postcode_input).to_be_hidden()
