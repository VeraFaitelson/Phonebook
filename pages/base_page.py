"""Base Page Object containing shared Selenium helper methods"""

from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    """Base class for all Page Objects. Wraps common WebDriver interactions"""


    def __init__(self, driver: WebDriver, timeout: int = 10):
        """Store WebDriver instance and create a reusable explicit wait object"""
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        """Waits until the element is visible on the page and returns it"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Waits until the element is clickable and performs a click"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def fill(self, locator, value: str):
        """Clears an input field and types the given text"""
        element = self.find(locator)
        element.clear()
        element.send_keys(value)

    def is_visible(self, locator, timeout: int = 5) -> bool:
        """Safely checks if an element becomes visible without raising an exception"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def get_alert_text(self) -> str:
        """Waits for a browser alert to appear and returns its text"""
        alert = self.wait.until(EC.alert_is_present())
        return alert.text

    def accept_alert(self):
        """Waits for a browser alert and clicks OK/Accept"""
        self.wait.until(EC.alert_is_present()).accept()
