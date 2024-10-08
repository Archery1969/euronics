import random
import string

from behave.configuration import Configuration
from playwright.sync_api import Locator, expect

global_timeout = 5000

expect.set_options(timeout=global_timeout)


def get_userdata_value(context, key: str, default=None):
    config: Configuration = context.config
    return config.userdata.get(key, default)


def perform_action(locator: Locator = None, action=None, fill_value=None):
    if action is not None:
        action = action.lower()
    if action == "click" and locator:
        locator.click(timeout=global_timeout)
    elif action == "fill" and locator and fill_value:
        locator.fill(fill_value, timeout=global_timeout)
    elif action == "type" and locator and fill_value:
        locator.type(fill_value, timeout=global_timeout)
    elif action == "press" and locator and fill_value:
        locator.press(fill_value, timeout=global_timeout)
    else:
        return locator


def generate_user_email(length=12, domain="gmail.com"):
    char_set = string.ascii_lowercase + string.digits
    username = random.choice(string.ascii_lowercase)
    username += ''.join(random.choices(char_set, k=length - 2))
    username += random.choice(string.ascii_lowercase)
    username += f'@{domain}'
    return username


def generate_random_password(length=12):
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice('!@#$%&*')
    all_characters = string.ascii_letters + string.digits + '!@#$%&*'
    remaining_length = length - 4
    random_chars = ''.join(random.choice(all_characters) for _ in range(remaining_length))
    password = upper + lower + digit + special + random_chars
    password = ''.join(random.sample(password, len(password)))
    return password
