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
