from behave import given, when, then
from playwright.sync_api import expect

from pages.login_page import LoginPage


@given(u'I am on the login page')
def step_impl(context):
    login_page = LoginPage(context.page)
    expect(login_page.page).to_have_title(login_page.page_title())


@when(u'I enter my email and password')
def step_impl(context):
    login_page = LoginPage(context.page)
    login_page.enter_email(action="fill", fill_value="user@example.com")
    login_page.enter_password(action="fill", fill_value="password123")


@when(u'I click the login button')
def step_impl(context):
    login_page = LoginPage(context.page)
    login_page.click_login_button(action="click")


@when(u'I click the forgot password link')
def step_impl(context):
    login_page = LoginPage(context.page)
    login_page.click_forgot_password_link(action="click")


@then(u'I should be logged in successfully')
def step_impl(context):
    login_page = LoginPage(context.page)
    expect(login_page.dashboard_locator()).to_be_visible()


@then(u'I should be taken to the password reset page')
def step_impl(context):
    login_page = LoginPage(context.page)
    expect(login_page.password_reset_page_locator()).to_be_visible()
