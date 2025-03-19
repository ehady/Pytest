import pytest
from selenium import webdriver
from tests.pages.login_page import LoginPage
from tests.pages.home_page import HomePage

@pytest.fixture
def driver():
    url = "https://www.saucedemo.com/"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    form = LoginPage(driver)
    home_page= HomePage(driver)
    form.enter_login_username("standard_user")
    form.enter_login_password("secret_sauce")
    form.click_login_button()

    assert form.check_login_status()

    yield driver

    home_page.click_logout_button()
