from behave import given, when, then
from playwright.sync_api import expect

from pages.checkout_guest_page import CheckoutGuestPage


@given(u'I am on the checkout page as a guest')
def step_impl(context):
    checkout_page = CheckoutGuestPage(context.page)
    expect(checkout_page.page).to_have_title(checkout_page.page_title())


@when(u'I enter my personal information')
def step_impl(context):
    checkout_page = CheckoutGuestPage(context.page)
    checkout_page.enter_personal_information(action="fill", fill_value="John Doe")


@when(u'I enter my delivery address')
def step_impl(context):
    checkout_page = CheckoutGuestPage(context.page)
    checkout_page.enter_delivery_address(action="fill", fill_value="123 Main St")


@when(u'I select a delivery date')
def step_impl(context):
    checkout_page = CheckoutGuestPage(context.page)
    checkout_page.select_delivery_date(action="click")


@when(u'I select "{payment_method}" as the payment method')
def step_impl(context, payment_method):
    checkout_page = CheckoutGuestPage(context.page)
    checkout_page.select_payment_method(action="click", fill_value=payment_method)


@when(u'I enter my payment details')
def step_impl(context):
    checkout_page = CheckoutGuestPage(context.page)
    checkout_page.enter_payment_details(action="fill", fill_value="Debit Card Details")


@when(u'I place the order')
def step_impl(context):
    checkout_page = CheckoutGuestPage(context.page)
    checkout_page.place_order_locator(action="click")


@then(u'I should be taken to the order confirmation page')
def step_impl(context):
    checkout_page = CheckoutGuestPage(context.page)
    expect(checkout_page.order_confirmation_locator()).to_be_visible()
