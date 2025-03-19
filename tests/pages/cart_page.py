from selenium.webdriver.common.by import By
from .common import CommonOps

class CartPage(CommonOps):

    def is_item_in_cart(self,item_name):
        xpath = f"//div[text()='{item_name}']"
        return self.is_element_present((By.XPATH,xpath))

