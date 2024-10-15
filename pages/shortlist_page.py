from playwright.sync_api import Page

from locators.shortlist_page_locators import ShortlistPageLocators
from utils.helper import perform_action


class ShortlistPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = ShortlistPageLocators(page)

    def page_title(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.page_title, action, fill_value)

    def product_list_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.product_list, action, fill_value)

    def remove_product_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.remove_product_button, action, fill_value)

    def move_to_basket_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.move_to_basket_button, action, fill_value)

    def basket_confirmation_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.basket_confirmation_message, action, fill_value)
