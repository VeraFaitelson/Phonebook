"""Base Page Object containing shared Selenium helper methods"""
import logging
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger(__name__)

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
        logger.debug("Click on %s", locator)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def fill(self, locator, value: str, mask: bool = False):
        """Clears an input field and types the given text"""
        display_value = "***" if mask else value
        logger.debug("Fill %s with '%s'", locator, display_value)
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
            logger.debug("Element %s not visible after %s seconds", locator, timeout)
            return False

    def get_alert_text(self) -> str:
        """Waits for a browser alert to appear and returns its text"""
        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        logger.debug("Alert appeared with text: '%s'", text)
        return text

    def accept_alert(self):
        """Waits for a browser alert and clicks OK/Accept"""
        logger.debug("Accepting browser alert")
        self.wait.until(EC.alert_is_present()).accept()
