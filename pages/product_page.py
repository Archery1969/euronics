from playwright.sync_api import Page

from locators.product_page_locators import ProductPageLocators
from utils.helper import perform_action


class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = ProductPageLocators(page)

    def page_title(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.page_title, action, fill_value)

    def product_name_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.product_name, action, fill_value)

    def product_description_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.product_description, action, fill_value)

    def product_image_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.product_image, action, fill_value)

    def product_price_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.product_price, action, fill_value)

    def product_variants_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.product_variants, action, fill_value)

    def add_to_shortlist_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.add_to_shortlist_button, action, fill_value)

    def add_to_basket_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.add_to_basket_button, action, fill_value)

    def shortlist_confirmation_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.shortlist_confirmation_message, action, fill_value)

    def basket_confirmation_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.basket_confirmation_message, action, fill_value)
