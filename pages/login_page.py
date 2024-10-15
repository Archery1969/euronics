from playwright.sync_api import Page

from locators.login_page_locators import LoginPageLocators
from utils.helper import perform_action


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = LoginPageLocators(page)

    def page_title(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.page_title, action, fill_value)

    def enter_email(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.email_input, action, fill_value)

    def enter_password(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.password_input, action, fill_value)

    def click_login_button(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.login_button, action, fill_value)

    def click_forgot_password_link(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.forgot_password_link, action, fill_value)

    def dashboard_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.dashboard, action, fill_value)

    def password_reset_page_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.password_reset_page, action, fill_value)
