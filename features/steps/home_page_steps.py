from behave import given, when, then
from playwright.sync_api import expect

from pages.home_page import HomePage
from utils.helper import global_timeout


@given(u'I am on the home page')
def step_impl(context):
    pass


@given(u'the cookie accept button is visible')
def step_impl(context):
    home_page = HomePage(context.page)
    expect(home_page.cookie_button_locator()).to_be_visible()


@when(u'I click the cookie accept button')
def step_impl(context):
    home_page = HomePage(context.page)
    home_page.cookie_button_locator().click(timeout=global_timeout)


@then(u'the cookie accept button should no longer be visible')
def step_impl(context):
    home_page = HomePage(context.page)
    expect(home_page.cookie_button_locator()).to_be_hidden()
