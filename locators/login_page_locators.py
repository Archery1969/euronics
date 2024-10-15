from playwright.sync_api import Page


class LoginPageLocators:
    def __init__(self, page: Page):
        self.page = page
        self.page_title = "Login"
        self.email_input = page.get_by_placeholder("Email Address")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Log In")
        self.forgot_password_link = page.get_by_role("link", name="Forgot Password")
        self.dashboard = page.get_by_role("heading", name="Dashboard")
        self.password_reset_page = page.get_by_role("heading", name="Password Reset")
