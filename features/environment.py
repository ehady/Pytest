import json
from selenium import webdriver
import os
from dotenv import load_dotenv
from tests.pages.login_page import LoginPage
from tests.pages.home_page import HomePage
from tests.pages.cart_page import CartPage


def before_all(context):
    load_dotenv()
    context.test_username = os.getenv("TEST_USERNAME")
    context.test_password = os.getenv("TEST_PASSWORD")
    context.base_url = os.getenv("TEST_URL")

    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.get(context.base_url)


def before_scenario(context, scenario):
    context.driver.get(context.base_url)

    if "single item" in scenario.name.lower():
        test_data_file = "features/test_data/test_data_single_item.json"
    elif "multiple items" in scenario.name.lower():
        test_data_file = "features/test_data/test_data_multiple_items.json"
    else:
        raise ValueError(f"No test data file assigned for scenario: {scenario.name}")

    with open(test_data_file) as f:
        context.test_data = json.load(f)

    context.login_page = LoginPage(context.driver)
    context.home_page = HomePage(context.driver)
    context.cart_page = CartPage(context.driver)


def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()
