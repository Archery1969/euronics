import random
import string

from behave.configuration import Configuration
from playwright.sync_api import Page, expect

from locators.home_page_locators import HomePageLocators

global_timeout = 5000

expect.set_options(timeout=global_timeout)


def home_page_locators(page: Page) -> HomePageLocators:
    return HomePageLocators(page)


def get_userdata_value(context, key: str, default=None):
    config: Configuration = context.config
    return config.userdata.get(key, default)


def generate_user_email(length=12, domain="gmail.com"):
    char_set = string.ascii_lowercase + string.digits
    username = random.choice(string.ascii_lowercase)
    username += ''.join(random.choices(char_set, k=length - 2))
    username += random.choice(string.ascii_lowercase)
    username += f'@{domain}'
    return username


def generate_user_password(length=12):
    char_set = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = random.choice(string.ascii_lowercase)
    password += ''.join(random.choices(char_set, k=length - 2))
    password += random.choice(string.ascii_lowercase)
    return password
