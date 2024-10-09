from playwright.sync_api import Page

from locators.contact_locators import ContactUsPageLocators


class ContactUsPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = ContactUsPageLocators(page)

    def page_title(self):
        return self.locators.page_title
