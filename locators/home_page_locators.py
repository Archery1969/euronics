from playwright.sync_api import Page


class HomePageLocators:
    def __init__(self, page: Page):
        self.page = page

        self.page_title = "Euronics Site | Buy Home and Kitchen Appliances Online | Euronics"
        self.cookie_accept_button = page.get_by_role("button", name="Accept All Cookies")
        self.postcode_input = page.get_by_placeholder("Enter your postcode")
        self.postcode_search_button = page.locator("#buyLocalForm").get_by_role("button")
        self.search_input = page.get_by_placeholder("Search for products")
        self.search_button = page.get_by_role("button", name="Search")
        self.header_link_my_account = page.get_by_role("link", name="My Account")
        self.header_link_store_finder = page.get_by_role("link", name="Store Finder")
        self.header_link_shortlist = page.get_by_role("link", name="Shortlist")
        self.header_link_basket = page.get_by_role("link", name="Basket")
        self.footer_link_about_us = page.get_by_role("link", name="About Us")
        self.footer_link_privacy_policy = page.get_by_role("link", name="Privacy Policy")
        self.footer_link_cookie_policy = page.get_by_role("link", name="Cookie Policy")
        self.footer_link_newsletter_signup = page.get_by_role("link", name="Newsletter Sign-up")
        self.page_about_us = page.get_by_text("About Us")
        self.page_privacy_policy = page.get_by_text("Privacy Policy")
        self.page_cookie_policy = page.get_by_text("Cookie Policy")
        self.page_newsletter_signup = page.get_by_text("Newsletter Sign-up")
