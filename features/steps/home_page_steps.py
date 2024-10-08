from behave import given

from utils.helper import *


@given(u'I am on the home page')
def step_impl(context):
    page: Page = context.page
    expect(page).to_have_title(home_page_locators(page).home_page_title)
