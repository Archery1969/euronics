from playwright.sync_api import Page


class BasketPageLocators:
    def __init__(self, page: Page):
        self.page = page
        self.page_title = "Basket"
        self.product_name = page.get_by_role("heading", name="Product Name")
        self.product_description = page.get_by_role("article", name="Product Description")
        self.product_price = page.get_by_role("heading", name="Price")
        self.product_quantity = page.get_by_role("spinbutton", name="Quantity")
        self.increase_quantity_button = page.get_by_role("button", name="Increase Quantity")
        self.decrease_quantity_button = page.get_by_role("button", name="Decrease Quantity")
        self.remove_product_button = page.get_by_role("button", name="Remove Product")
        self.proceed_to_checkout_button = page.get_by_role("button", name="Proceed to Checkout")
        self.checkout_page = page.get_by_role("heading", name="Checkout")
