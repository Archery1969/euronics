from playwright.sync_api import Page

from locators.catalogue_page_locators import CataloguePageLocators


class CheckoutGuestPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = CataloguePageLocators(page)
