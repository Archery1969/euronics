from behave import given, when, then
from playwright.sync_api import expect

from pages.home_page import HomePage


@given(u'I am on the homepage')
def step_impl(context):
    home_page = HomePage(context.page)
    expect(home_page.page).to_have_title(home_page.page_title())


@when(u'I search for a product by category, name, or SKU')
def step_impl(context):
    home_page = HomePage(context.page)
    home_page.search_product_locator(action="fill", fill_value="Sample Product")
    home_page.search_button_locator(action="click")


@then(u'I should see products related to the searched input')
def step_impl(context):
    home_page = HomePage(context.page)
    expect(home_page.product_list_locator()).to_be_visible()


@when(u'I click on the my account header link')
def step_impl(context):
    home_page = HomePage(context.page)
    home_page.header_link_my_account(action="click")


@when(u'I click on the store finder header link')
def step_impl(context):
    home_page = HomePage(context.page)
    home_page.header_link_store_finder(action="click")


@when(u'I click on the shortlist header link')
def step_impl(context):
    home_page = HomePage(context.page)
    home_page.header_link_shortlist(action="click")


@when(u'I click on the basket header link')
def step_impl(context):
    home_page = HomePage(context.page)
    home_page.header_link_basket(action="click")


@when(u'I click on the about us footer link')
def step_impl(context):
    home_page = HomePage(context.page)
    home_page.footer_link_about_us(action="click")


@when(u'I click on the privacy policy footer link')
def step_impl(context):
    home_page = HomePage(context.page)
    home_page.footer_link_privacy_policy(action="click")


@when(u'I click on the cookie policy footer link')
def step_impl(context):
    home_page = HomePage(context.page)
    home_page.footer_link_cookie_policy(action="click")


@when(u'I click on the newsletter sign-up footer link')
def step_impl(context):
    home_page = HomePage(context.page)
    home_page.footer_link_newsletter_signup(action="click")


@then(u'I should be taken to the login page')
def step_impl(context):
    home_page = HomePage(context.page)
    expect(home_page.login_page_locator()).to_be_visible()


@then(u'I should be taken to the store finder page')
def step_impl(context):
    home_page = HomePage(context.page)
    expect(home_page.store_finder_page_locator()).to_be_visible()


@then(u'I should be taken to the shortlist page')
def step_impl(context):
    home_page = HomePage(context.page)
    expect(home_page.shortlist_page_locator()).to_be_visible()


@then(u'I should be taken to the basket page')
def step_impl(context):
    home_page = HomePage(context.page)
    expect(home_page.basket_page_locator()).to_be_visible()


@then(u'I should see the About Us page')
def step_impl(context):
    home_page = HomePage(context.page)
    expect(home_page.page_about_us()).to_be_visible()


@then(u'I should see the Privacy Policy page')
def step_impl(context):
    home_page = HomePage(context.page)
    expect(home_page.page_privacy_policy()).to_be_visible()


@then(u'I should see the Cookie Policy page')
def step_impl(context):
    home_page = HomePage(context.page)
    expect(home_page.page_cookie_policy()).to_be_visible()


@then(u'I should see the Newsletter Sign-up page')
def step_impl(context):
    home_page = HomePage(context.page)
    expect(home_page.page_newsletter_signup()).to_be_visible()
