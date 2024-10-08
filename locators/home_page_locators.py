from playwright.sync_api import Page


class HomePageLocators:
    def __init__(self, page: Page):
        self.page = page

        self.home_page_title = "Euronics Site | Buy Home and Kitchen Appliances Online | Euronics"
        self.cookie_accept_button = page.get_by_role("button", name="Accept All Cookies")
        self.postcode_input = page.get_by_placeholder("Enter your postcode")
        self.postcode_search_button = page.locator("#buyLocalForm").get_by_role("button")
        self.contact_us_link = page.get_by_role("link", name="Contact Us")
        self.contact_us_page_title = "Contact Us | Euronics Site"
        self.faq_link = page.get_by_role("link", name="FAQs")
        self.faq_page_title = "FAQs | Euronics Site"
        self.delivery_link = page.get_by_role("link", name="Delivery & Installation")
        self.delivery_page = "Terms of Sale | Euronics Site"
