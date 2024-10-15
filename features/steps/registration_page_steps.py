from behave import given, when, then
from playwright.sync_api import expect

from pages.registration_page import RegistrationPage


@given(u'I am on the registration page')
def step_impl(context):
    registration_page = RegistrationPage(context.page)
    expect(registration_page.page).to_have_title(registration_page.page_title())


@when(u'I enter my title, first name, last name, email, and password')
def step_impl(context):
    registration_page = RegistrationPage(context.page)
    registration_page.enter_title(action="fill", fill_value="Mr")
    registration_page.enter_first_name(action="fill", fill_value="John")
    registration_page.enter_last_name(action="fill", fill_value="Doe")
    registration_page.enter_email(action="fill", fill_value="john.doe@example.com")
    registration_page.enter_password(action="fill", fill_value="password123")


@when(u'I confirm my password')
def step_impl(context):
    registration_page = RegistrationPage(context.page)
    registration_page.confirm_password(action="fill", fill_value="password123")


@when(u'I click the create account button')
def step_impl(context):
    registration_page = RegistrationPage(context.page)
    registration_page.click_create_account_button(action="click")


@then(u'My new account should be created successfully')
def step_impl(context):
    registration_page = RegistrationPage(context.page)
    expect(registration_page.success_message_locator()).to_be_visible()
