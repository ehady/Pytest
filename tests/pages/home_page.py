from selenium.webdriver.common.by import By
from .common import CommonOps

class HomePage(CommonOps):
    GO_TO_CART_BTN = (By.ID, "shopping_cart_container")
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_BTN = (By.ID, "logout_sidebar_link")

    def navigate_to_cart(self):
        self.wait_for(self.GO_TO_CART_BTN).click()

    def click_add_to_cart_button(self, item_name):
        item_name = item_name.lower().replace(" ", "-")
        locator = (By.XPATH, f"//button[@id='add-to-cart-{item_name}']")
        self.wait_for(locator).click()

    def click_logout_button(self):
        self.wait_for(self.MENU_BTN).click()
        self.wait_for(self.LOGOUT_BTN).click()

