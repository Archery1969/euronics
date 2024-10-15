from playwright.sync_api import Page


class RegistrationPageLocators:
    def __init__(self, page: Page):
        self.page = page
        self.page_title = "Registration"
        self.title_input = page.get_by_placeholder("Title")
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.email_input = page.get_by_placeholder("Email")
        self.password_input = page.get_by_placeholder("Password")
        self.confirm_password_input = page.get_by_placeholder("Confirm Password")
        self.create_account_button = page.get_by_role("button", name="Create Account")
        self.success_message = page.get_by_text("Account created successfully")
