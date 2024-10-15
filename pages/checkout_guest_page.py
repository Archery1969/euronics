from playwright.sync_api import Page

from locators.checkout_guest_page_locators import CheckoutGuestPageLocators
from utils.helper import perform_action


class CheckoutGuestPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = CheckoutGuestPageLocators(page)

    def page_title(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.page_title, action, fill_value)

    def enter_personal_information(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.personal_information, action, fill_value)

    def enter_delivery_address(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.delivery_address, action, fill_value)

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
