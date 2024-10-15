from playwright.sync_api import Page


class AccountPageLocators:
    def __init__(self, page: Page):
        self.page = page
        self.page_title = "Account Page"
        self.order_history = page.get_by_role("heading", name="Order History")
        self.user_details = page.get_by_role("textbox", name="User Details")
        self.address_book = page.get_by_role("heading", name="Address Book")
        self.address_input = page.get_by_role("textbox", name="New Address")
        self.success_message = page.get_by_text("Details updated successfully")
        self.updated_address = page.get_by_text("Updated Address")
