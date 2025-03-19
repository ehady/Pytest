from selenium.webdriver.common.by import By
from .common import CommonOps

class LoginPage(CommonOps):
    FORM_USERNAME = (By.ID, "user-name")
    FORM_PASSWORD = (By.ID, "password")
    FORM_SUBMIT_BTN = (By.ID, "login-button")
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    FORM_ERROR = (By.XPATH, "//h3[@data-test='error']")

    def enter_login_username(self,username):
        self.wait_for(self.FORM_USERNAME).send_keys(username)

    def enter_login_password(self,password):
        self.wait_for(self.FORM_PASSWORD).send_keys(password)

    def click_login_button(self):
        self.wait_for(self.FORM_SUBMIT_BTN).click()

    def check_login_status(self):
        if self.is_element_present(self.FORM_ERROR):
            return False  # Login failed

        return self.is_element_present(self.MENU_BTN)  # Login success if menu button is present

