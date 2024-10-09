from playwright.sync_api import Page

from locators.home_page_locators import HomePageLocators


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = HomePageLocators(page)

    def homepage_title(self):
        return self.locators.page_title

    def cookie_button_locator(self):
        return self.locators.cookie_accept_button

    def postcode_input_locator(self):
        return self.locators.postcode_input

    def postcode_search_locator(self):
        return self.locators.postcode_search_button
