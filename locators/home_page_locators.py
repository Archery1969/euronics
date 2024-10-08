from playwright.sync_api import Page


class HomePageLocators:
    def __init__(self, page: Page):
        self.page = page

        self.home_page_title = "Euronics Site | Buy Home and Kitchen Appliances Online | Euronics"
        self.cookie_accept_button = page.get_by_role("button", name="Accept All Cookies")
