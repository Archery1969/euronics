from playwright.sync_api import Locator


def perform_action(locator: Locator = None, action: str = '', fill_value=None):
    action = action.lower()
    if action == 'visible' and locator:
        return locator
    elif action == 'hidden' and locator:
        return locator
    elif action == 'click' and locator:
        locator.click()
    elif action == 'fill' and locator and fill_value:
        locator.fill(fill_value)
    else:
        raise ValueError(f"Action '{action}' is not supported for this element.")
