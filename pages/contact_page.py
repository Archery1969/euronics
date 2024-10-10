from playwright.sync_api import Page

from locators.contact_page_locators import ContactPageLocators


class ContactPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = ContactPageLocators(page)

    def page_title(self):
        return self.locators.page_title
