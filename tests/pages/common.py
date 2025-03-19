from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

class CommonOps:
    def __init__(self,driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)

    def wait_for(self,locator):
        return self._wait.until(ec.presence_of_element_located(locator))

    def find(self,locator):
        return self.driver.find_element(*locator)

    def is_element_present(self, locator):
        try:
            self.find(locator)
            return True

        except NoSuchElementException:
            return False
