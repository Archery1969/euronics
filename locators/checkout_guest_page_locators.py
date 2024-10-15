from playwright.sync_api import Page


class CheckoutGuestPageLocators:
    def __init__(self, page: Page):
        self.page = page
        self.page_title = "Guest Checkout"
        self.personal_information = page.get_by_placeholder("Enter your personal information")
        self.delivery_address = page.get_by_placeholder("Enter your delivery address")
        self.delivery_date = page.get_by_role("combobox", name="Delivery Date")
        self.payment_method = page.get_by_role("button", name="Payment Method")
        self.payment_details = page.get_by_role("textbox", name="Payment Details")
        self.place_order_button = page.get_by_role("button", name="Place Order")
        self.order_confirmation = page.get_by_role("heading", name="Order Confirmation")
