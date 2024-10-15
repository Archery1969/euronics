from playwright.sync_api import Page

from locators.basket_page_locators import BasketPageLocators
from utils.helper import perform_action


class BasketPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = BasketPageLocators(page)

    def page_title(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.page_title, action, fill_value)

    def product_name_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.product_name, action, fill_value)

    def product_description_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.product_description, action, fill_value)

    def product_price_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.product_price, action, fill_value)

    def product_quantity_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.product_quantity, action, fill_value)

    def increase_quantity_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.increase_quantity_button, action, fill_value)

    def decrease_quantity_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.decrease_quantity_button, action, fill_value)

    def remove_product_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.remove_product_button, action, fill_value)

    def proceed_to_checkout_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.proceed_to_checkout_button, action, fill_value)

    def checkout_page_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.checkout_page, action, fill_value)
