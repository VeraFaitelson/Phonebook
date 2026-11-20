"""Pytest fixtures for browser setup and user authentication."""

import pytest
from selenium import webdriver

from models.user import User
from pages.login_page import LoginPage

BASE_URL = "https://telranedu.pages.dev"
DEFAULT_USER = User("qa_portfolio_user@gmail.com", "TestPass!12345")


@pytest.fixture
def driver():
    """Initializes Chrome WebDriver before a test and closes it afterward."""
    # SETUP: executed BEFORE launching the test
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(BASE_URL)

    # Pause fixture execution and pass the browser instance to the test
    yield browser

    # TEARDOWN: executed AFTER the test finishes (even if it fails)
    browser.quit()

@pytest.fixture
def authenticated(driver):
    """Logs in as the default test user and returns the authenticated driver"""
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_login_form(DEFAULT_USER)
    login_page.click_on_login_button()

    # Fail fast if login failed during setup
    assert login_page.is_sign_out_displayed(), "Failed to log in inside 'authenticated' fixture"

    return driver
