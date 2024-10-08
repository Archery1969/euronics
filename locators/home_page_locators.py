from playwright.sync_api import Page


class HomePageLocators:
    def __init__(self, page: Page):
        self.page = page

        self.home_page_title = page.locator("title").first.text_content()
        self.cookie_accept_button = page.get_by_role("button", name="Accept All Cookies")
