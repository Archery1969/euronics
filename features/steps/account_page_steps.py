from behave import given, when, then
from playwright.sync_api import expect

from pages.account_page import AccountPage


@given(u'I am on the account page')
def step_impl(context):
    account_page = AccountPage(context.page)
    expect(account_page.page).to_have_title(account_page.page_title())


@when(u'I view my order history')
def step_impl(context):
    account_page = AccountPage(context.page)
    expect(account_page.order_history_locator()).to_be_visible()


@when(u'I update my user details')
def step_impl(context):
    account_page = AccountPage(context.page)
    account_page.update_user_details(action="fill", fill_value="New User Details")


@when(u'I view my address book')
def step_impl(context):
    account_page = AccountPage(context.page)
    expect(account_page.address_book_locator()).to_be_visible()


@when(u'I update my address')
def step_impl(context):
    account_page = AccountPage(context.page)
    account_page.update_address(action="fill", fill_value="New Address")


@then(u'I should see my previous orders')
def step_impl(context):
    account_page = AccountPage(context.page)
    expect(account_page.order_history_locator()).to_have_text("Previous Orders")


@then(u'My details should be saved successfully')
def step_impl(context):
    account_page = AccountPage(context.page)
    expect(account_page.success_message_locator()).to_be_visible()


@then(u'The updated address should be saved')
def step_impl(context):
    account_page = AccountPage(context.page)
    expect(account_page.updated_address_locator()).to_be_visible()
