import allure
import yaml
from behave.configuration import Configuration
from playwright.sync_api import sync_playwright


def before_all(context):
    print("before_all: Starting Playwright setup...")
    try:
        context.driver = sync_playwright().start()
        context.browser = context.driver.chromium.launch(headless=False, slow_mo=1000, channel="chrome")
        env = context.config.userdata.get("ENV", "dev").lower()
        config_file = f"config/config_{env}.yml"
        with open(config_file, 'r') as config_file:
            config_data = yaml.safe_load(config_file)
        context.config.userdata.update(config_data)
    except Exception as e:
        raise AssertionError(e)


def before_scenario(context, scenario):
    try:
        print(f"Running scenario: {scenario.name}")
        context.page = context.browser.new_page()
        config: Configuration = context.config
        context.page.goto(config.userdata["storefront_url"])
    except Exception as e:
        raise AssertionError(e)


def before_step(context, step):
    context.step = step


def after_step(context, step):
    if step.status == "failed":
        try:
            screenshot_bytes = context.page.screenshot()
            allure.attach(screenshot_bytes, name="screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            raise AssertionError(e)


def after_scenario(context, scenario):
    try:
        context.page.close()
    except Exception as e:
        raise AssertionError(e)


def after_all(context):
    try:
        context.browser.close()
        context.driver.stop()
    except Exception as e:
        raise AssertionError(e)
