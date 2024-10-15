from playwright.sync_api import Page


class CheckoutLoggedInPageLocators:
    def __init__(self, page: Page):
        self.page = page
        self.login_page_title = "Login Page"
        self.email_input = page.get_by_placeholder("Email Address")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Log In")
        self.proceed_to_checkout_button = page.get_by_role("button", name="Proceed to Checkout")
        self.checkout_page_title = "Checkout Page"
        self.saved_delivery_address = page.get_by_role("button", name="Saved Delivery Address")
        self.delivery_date = page.get_by_role("combobox", name="Delivery Date")
        self.payment_method = page.get_by_role("button", name="Payment Method")
        self.payment_details = page.get_by_role("textbox", name="Payment Details")
        self.place_order_button = page.get_by_role("button", name="Place Order")
        self.order_confirmation = page.get_by_role("heading", name="Order Confirmation")
