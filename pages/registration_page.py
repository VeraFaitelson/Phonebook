"""Page Object for the Registration page"""

from selenium.webdriver.common.by import By

from models.user import User
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    """Encapsulates locators and actions for creating a new user account"""

    # Locators (registration and login share the same tab on this site)
    REGISTRATION_LINK = (By.XPATH, "//a[text()='LOGIN']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "button[name='registration']")
    SIGN_OUT_BUTTON = (By.XPATH, "//*[text()='Sign Out']")

    def open_registration_page(self):
        """Navigates to the Login/Registration tab"""
        self.click(self.REGISTRATION_LINK)

    def fill_email_field(self, email: str):
        """Enters email into the registration email input field"""
        self.fill(self.EMAIL_INPUT, email)

    def fill_password_field(self, password: str):
        """Enters password into the registration password input field"""
        self.fill(self.PASSWORD_INPUT, password)

    def fill_registration_form(self, user: User):
        """Fills both email and password fields using a User model"""
        self.fill_email_field(user.email)
        self.fill_password_field(user.password)

    def click_on_registration_button(self):
        """Clicks the Registration submit button"""
        self.click(self.BUTTON_REGISTRATION)

    def is_sign_out_displayed(self) -> bool:
        """Checks if the 'Sign Out' button is visible (confirms successful registration)"""
        return self.is_visible(self.SIGN_OUT_BUTTON)
