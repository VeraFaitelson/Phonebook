"""Tests for user registration functionality (positive and negative scenarios)"""

from conftest import DEFAULT_USER
from models.user import User
from pages.registration_page import RegistrationPage
from utils.data_generator import generate_unique_email

# Test data constants for negative scenarios
INVALID_EMAIL = "testQAgmailcom"
INVALID_PASSWORD = "test"


def test_valid_registration_success(driver):
    """Verify successful registration with a unique email and valid password"""
    registration_page = RegistrationPage(driver)
    user = User(generate_unique_email(), DEFAULT_USER.password)

    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)
    registration_page.click_on_registration_button()

    assert registration_page.is_sign_out_displayed()


def test_registration_with_invalid_email_and_valid_password(driver):
    """Verify validation alert appears when registering with an invalid email format"""
    registration_page = RegistrationPage(driver)
    user = User(INVALID_EMAIL, DEFAULT_USER.password)

    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)
    registration_page.click_on_registration_button()

    alert_text = registration_page.get_alert_text()
    assert "Wrong email or password format" in alert_text
    registration_page.accept_alert()


def test_registration_with_valid_email_and_invalid_password(driver):
    """Verify validation alert appears when registering with a weak password"""
    registration_page = RegistrationPage(driver)
    user = User(generate_unique_email(), INVALID_PASSWORD)

    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)
    registration_page.click_on_registration_button()

    alert_text = registration_page.get_alert_text()
    assert "Wrong email or password format" in alert_text
    registration_page.accept_alert()


def test_registration_with_already_exist_email(driver):
    """Verify error alert appears when registering with an already registered email"""
    registration_page = RegistrationPage(driver)

    registration_page.open_registration_page()
    registration_page.fill_registration_form(DEFAULT_USER)
    registration_page.click_on_registration_button()

    alert_text = registration_page.get_alert_text()
    assert alert_text == "User already exist"
    registration_page.accept_alert()
