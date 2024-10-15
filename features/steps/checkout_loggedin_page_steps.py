from behave import given, when
from playwright.sync_api import expect

from pages.checkout_loggedin_page import CheckoutLoggedInPage


@when(u'I log in with my email and password')
def step_impl(context):
    checkout_page = CheckoutLoggedInPage(context.page)
    checkout_page.enter_email(action="fill", fill_value="user@example.com")
    checkout_page.enter_password(action="fill", fill_value="password123")
    checkout_page.click_login_button(action="click")


@given(u'I am on the checkout page as a logged-in user')
def step_impl(context):
    checkout_page = CheckoutLoggedInPage(context.page)
    expect(checkout_page.page).to_have_title(checkout_page.checkout_page_title())


@when(u'I select my saved delivery address')
def step_impl(context):
    checkout_page = CheckoutLoggedInPage(context.page)
    checkout_page.select_saved_delivery_address(action="click")
