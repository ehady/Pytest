from tests.pages.cart_page import CartPage
from tests.pages.home_page import HomePage

def test_add_item_to_cart(logged_in_driver):
    home_page = HomePage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)
    home_page.click_add_to_cart_button("Sauce Labs Backpack")
    home_page.navigate_to_cart()
    assert cart_page.is_item_in_cart("Sauce Labs Backpack")

def test_add_multiple_items_to_cart(logged_in_driver):
    home_page = HomePage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)
    home_page.click_add_to_cart_button("Sauce Labs Backpack")
    home_page.click_add_to_cart_button("Sauce Labs Bike Light")
    home_page.navigate_to_cart()
    assert cart_page.is_item_in_cart("Sauce Labs Backpack")
    assert cart_page.is_item_in_cart("Sauce Labs Bike Light")
