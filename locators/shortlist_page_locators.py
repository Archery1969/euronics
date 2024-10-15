from playwright.sync_api import Page


class ShortlistPageLocators:
    def __init__(self, page: Page):
        self.page = page
        self.page_title = "Shortlist"
        self.product_list = page.get_by_role("list", name="Shortlist Products")
        self.remove_product_button = page.get_by_role("button", name="Remove Product")
        self.move_to_basket_button = page.get_by_role("button", name="Move to Basket")
        self.basket_confirmation_message = page.get_by_text("Product added to basket")
