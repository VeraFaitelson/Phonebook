"""Tests for user login functionality (positive and negative scenarios)"""

from conftest import DEFAULT_USER
from models.user import User
from pages.login_page import LoginPage

# Test data constants for negative scenarios
INVALID_EMAIL = "testQAgmailcom"
INVALID_PASSWORD = "test"
UNREGISTERED_EMAIL = "testQA@gmail.com"


def test_valid_login_success(driver):
    """Verify successful login with valid credentials"""
    login_page = LoginPage(driver)

    login_page.open_login_page()
    login_page.fill_login_form(DEFAULT_USER)
    login_page.click_on_login_button()

    assert login_page.is_sign_out_displayed()


def test_with_invalid_email_and_valid_password(driver):
    """Verify error alert appears when email format is invalid"""
    login_page = LoginPage(driver)
    user = User(INVALID_EMAIL, DEFAULT_USER.password)

    login_page.open_login_page()
    login_page.fill_login_form(user)
    login_page.click_on_login_button()

    alert_text = login_page.get_alert_text()
    assert "Wrong email or password" in alert_text
    login_page.accept_alert()


def test_with_valid_email_and_invalid_password(driver):
    """Verify error alert appears when password is incorrect"""
    login_page = LoginPage(driver)
    user = User(DEFAULT_USER.email, INVALID_PASSWORD)

    login_page.open_login_page()
    login_page.fill_login_form(user)
    login_page.click_on_login_button()

    alert_text = login_page.get_alert_text()
    assert alert_text == "Wrong email or password"
    login_page.accept_alert()


def test_login_unregistered_user(driver):
    """Verify error alert appears for a non-existent user"""
    login_page = LoginPage(driver)
    user = User(UNREGISTERED_EMAIL, DEFAULT_USER.password)

    login_page.open_login_page()
    login_page.fill_login_form(user)
    login_page.click_on_login_button()

    alert_text = login_page.get_alert_text()
    assert alert_text == "Wrong email or password"
    login_page.accept_alert()
