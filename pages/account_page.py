from playwright.sync_api import Page

from locators.account_page_locators import AccountPageLocators
from utils.helper import perform_action


class AccountPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = AccountPageLocators(page)

    def page_title(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.page_title, action, fill_value)

    def order_history_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.order_history, action, fill_value)

    def update_user_details(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.user_details, action, fill_value)

    def address_book_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.address_book, action, fill_value)

    def update_address(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.address_input, action, fill_value)

    def success_message_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.success_message, action, fill_value)

    def updated_address_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.updated_address, action, fill_value)
