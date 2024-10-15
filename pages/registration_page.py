from playwright.sync_api import Page

from locators.registration_page_locators import RegistrationPageLocators
from utils.helper import perform_action


class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = RegistrationPageLocators(page)

    def page_title(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.page_title, action, fill_value)

    def enter_title(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.title_input, action, fill_value)

    def enter_first_name(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.first_name_input, action, fill_value)

    def enter_last_name(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.last_name_input, action, fill_value)

    def enter_email(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.email_input, action, fill_value)

    def enter_password(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.password_input, action, fill_value)

    def confirm_password(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.confirm_password_input, action, fill_value)

    def click_create_account_button(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.create_account_button, action, fill_value)

    def success_message_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.success_message, action, fill_value)
