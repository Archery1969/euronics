from playwright.sync_api import Page


class ProductPageLocators:
    def __init__(self, page: Page):
        self.page = page
        self.page_title = "Product Details"
        self.product_name = page.get_by_role("heading", name="Product Name")
        self.product_description = page.get_by_role("article", name="Product Description")
        self.product_image = page.get_by_role("img", name="Product Image")
        self.product_price = page.get_by_role("heading", name="Price")
        self.product_variants = page.get_by_role("list", name="Product Variants")
        self.add_to_shortlist_button = page.get_by_role("button", name="Add to Shortlist")
        self.add_to_basket_button = page.get_by_role("button", name="Add to Basket")
        self.shortlist_confirmation_message = page.get_by_text("Product added to shortlist")
        self.basket_confirmation_message = page.get_by_text("Product added to basket")
