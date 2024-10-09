import allure
import yaml
from playwright.sync_api import sync_playwright


def before_all(context):
    try:
        context.driver = sync_playwright().start()
        context.browser = context.driver.chromium.launch(headless=False, slow_mo=10, channel="chrome")

        # Load environment configuration
        env = context.config.userdata.get("ENV", "dev").lower()
        config_file = f"config/config_{env}.yml"
        with open(config_file, 'r') as file:
            config_data = yaml.safe_load(file)
        context.config.userdata.update(config_data)
    except Exception as e:
        raise AssertionError(f"Error in before_all setup: {e}")


def before_scenario(context, scenario):
    try:
        context.page = context.browser.new_page()
        storefront_url = context.config.userdata.get("storefront_url")
        if storefront_url:
            context.page.goto(storefront_url)
        else:
            raise ValueError("Storefront URL not found in configuration.")
    except Exception as e:
        raise AssertionError(f"Error in before_scenario setup: {e}")


def before_step(context, step):
    context.step = step


def after_step(context, step):
    if step.status == "failed":
        try:
            screenshot_bytes = context.page.screenshot()
            allure.attach(screenshot_bytes, name="screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f"Error taking screenshot: {e}")


def after_scenario(context, scenario):
    try:
        if hasattr(context, 'page'):
            context.page.close()
    except Exception as e:
        print(f"Error closing the page after scenario: {e}")


def after_all(context):
    try:
        if hasattr(context, 'browser'):
            context.browser.close()
        if hasattr(context, 'driver'):
            context.driver.stop()
    except Exception as e:
        print(f"Error in after_all teardown: {e}")
