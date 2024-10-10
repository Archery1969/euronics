from playwright.sync_api import Page


class HomePageLocators:
    def __init__(self, page: Page):
        self.page = page

        self.page_title = "Euronics Site | Buy Home and Kitchen Appliances Online | Euronics"
        self.cookie_accept_button = page.get_by_role("button", name="Accept All Cookies")
        self.postcode_input = page.get_by_placeholder("Enter your postcode")
        self.postcode_search_button = page.locator("#buyLocalForm").get_by_role("button")
