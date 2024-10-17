from playwright.sync_api import Page

from locators.home_page_locators import HomePageLocators
from utils.helper import perform_action


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = HomePageLocators(page)

    def navigate_to_storefront(self, url: str):
        self.page.goto(url)

    def page_title(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.page_title, action, fill_value)

    def cookie_button_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.cookie_accept_button, action, fill_value)

    def postcode_input_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.postcode_input, action, fill_value)

    def postcode_search_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.postcode_search_button, action, fill_value)

    def search_product_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.search_input, action, fill_value)

    def search_button_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.search_button, action, fill_value)

    def header_link_my_account(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.header_link_my_account, action, fill_value)

    def header_link_store_finder(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.header_link_store_finder, action, fill_value)

    def header_link_shortlist(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.header_link_shortlist, action, fill_value)

    def header_link_basket(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.header_link_basket, action, fill_value)

    def footer_link_about_us(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.footer_link_about_us, action, fill_value)

    def footer_link_privacy_policy(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.footer_link_privacy_policy, action, fill_value)

    def footer_link_cookie_policy(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.footer_link_cookie_policy, action, fill_value)

    def footer_link_newsletter_signup(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.footer_link_newsletter_signup, action, fill_value)

    def login_page_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.login_page, action, fill_value)

    def store_finder_page_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.store_finder_page, action, fill_value)

    def shortlist_page_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.shortlist_page, action, fill_value)

    def basket_page_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.basket_page, action, fill_value)

    def page_about_us(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.page_about_us, action, fill_value)

    def page_privacy_policy(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.page_privacy_policy, action, fill_value)

    def page_cookie_policy(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.page_cookie_policy, action, fill_value)

    def page_newsletter_signup(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.page_newsletter_signup, action, fill_value)
