from playwright.sync_api import Page

from locators.home_page_locators import HomePageLocators
from utils.actions import perform_action


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = HomePageLocators(page)

    def page_title(self):
        return self.locators.page_title

    def cookie_button_locator(self, action='visible'):
        return perform_action(self.locators.cookie_accept_button, action)

    def postcode_input_locator(self, action='visible', fill_value=None):
        return perform_action(self.locators.postcode_input, action, fill_value)

    def postcode_search_locator(self, action='visible'):
        return perform_action(self.locators.postcode_search_button, action)

    def contact_us_locator(self, action='visible'):
        return perform_action(self.locators.contact_us_link, action)
