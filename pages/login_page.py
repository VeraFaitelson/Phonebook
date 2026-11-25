"""Page Object for the Login page"""
import logging

from selenium.webdriver.common.by import By
from models.user import User
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class LoginPage(BasePage):
    """Encapsulates locators and actions for user authentication"""

    # Locators
    LOGIN_LINK = (By.XPATH, "//a[text()='LOGIN']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "button[name='login']")
    SIGN_OUT_BUTTON = (By.XPATH, "//*[text()='Sign Out']")

    def open_login_page(self):
        """Navigates to the Login tab"""
        logger.info("Opening Login form")
        self.click(self.LOGIN_LINK)

    def fill_email_field(self, email: str):
        """Enters email into the email input field"""
        self.fill(self.EMAIL_INPUT, email)

    def fill_password_field(self, password: str):
        """Enters password into the password input field"""
        self.fill(self.PASSWORD_INPUT, password, mask=True)

    def fill_login_form(self, user: User):
        """Fills both email and password fields using a User model"""
        logger.info("Filling login form for user: %s", user.email)
        self.fill_email_field(user.email)
        self.fill_password_field(user.password)

    def click_on_login_button(self):
        """Clicks the Login submit button"""
        self.click(self.BUTTON_LOGIN)

    def is_sign_out_displayed(self) -> bool:
        """Checks if the 'Sign Out' button is visible (confirms successful login)"""
        visible = self.is_visible(self.SIGN_OUT_BUTTON)
        logger.debug("Sign Out button displayed: %s", visible)
        return visible
