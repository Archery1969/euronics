from playwright.sync_api import Locator


def perform_action(locator: Locator = None, action=None, fill_value=None):
    action = action.lower()
    if action == 'click' and locator:
        locator.click()
    elif action == 'fill' and locator and fill_value:
        locator.fill(fill_value)
    else:
        return locator
