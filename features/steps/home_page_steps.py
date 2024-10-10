from behave import given, when, then

from pages.contact_page import ContactUsPage
from pages.home_page import HomePage
from utils.helper import *


@given(u'I am on the home page')
def step_impl(context):
    home_page = HomePage(context.page)
    expect(home_page.page).to_have_title(home_page.page_title())


@given(u'the cookie accept button is visible')
def step_impl(context):
    home_page = HomePage(context.page)
    home_page.cookie_button_locator(action='visible')


@when(u'I click the cookie accept button')
def step_impl(context):
    home_page = HomePage(context.page)
    home_page.cookie_button_locator(action='click')


@then(u'the cookie accept button should no longer be visible')
def step_impl(context):
    home_page = HomePage(context.page)
    home_page.cookie_button_locator(action='hidden')


@then(u'the postcode search input is visible')
def step_impl(context):
    home_page = HomePage(context.page)
    home_page.postcode_input_locator(action='visible')


@when(u'I enter a postcode')
def step_impl(context):
    home_page = HomePage(context.page)
    home_page.postcode_input_locator(action='fill', fill_value=context.config.userdata.get("storefront_postcode"))
    home_page.postcode_search_locator(action='click')


@then(u'the postcode search input should no longer be visible')
def step_impl(context):
    home_page = HomePage(context.page)
    home_page.postcode_input_locator(action='hidden')


@when(u'I click the contact is link')
def step_impl(context):
    home_page = HomePage(context.page)
    home_page.contact_us_locator(action='click')


@then(u'I am navigated to the contact us page')
def step_impl(context):
    contact_us_page = ContactUsPage(context.page)
    expect(contact_us_page.page).to_have_title(contact_us_page.page_title())
