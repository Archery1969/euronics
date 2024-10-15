from playwright.sync_api import Page

from locators.checkout_loggedin_page_locators import CheckoutLoggedInPageLocators
from utils.helper import perform_action


class CheckoutLoggedInPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = CheckoutLoggedInPageLocators(page)

    def login_page_title(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.login_page_title, action, fill_value)

    def enter_email(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.email_input, action, fill_value)

    def enter_password(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.password_input, action, fill_value)

    def click_login_button(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.login_button, action, fill_value)

    def proceed_to_checkout(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.proceed_to_checkout_button, action, fill_value)

    def checkout_page_title(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.checkout_page_title, action, fill_value)

    def select_saved_delivery_address(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.saved_delivery_address, action, fill_value)

    def select_delivery_date(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.delivery_date, action, fill_value)

    def select_payment_method(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.payment_method, action, fill_value)

    def enter_payment_details(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.payment_details, action, fill_value)

    def place_order_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.place_order_button, action, fill_value)

    def order_confirmation_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.order_confirmation, action, fill_value)
