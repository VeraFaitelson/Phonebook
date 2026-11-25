"""Pytest fixtures for browser setup and user authentication"""

import logging
import pytest
from selenium import webdriver

from models.user import User
from pages.login_page import LoginPage
from pages.contacts_page import ContactsPage
from pages.add_contact_page import ContactPage
from utils.data_generator import generate_contact
from utils.logger_config import configure_logger

BASE_URL = "https://telranedu.pages.dev"
DEFAULT_USER = User("qa_portfolio_user@gmail.com", "TestPass!12345")

configure_logger()
logger = logging.getLogger(__name__)


@pytest.fixture
def driver(request):
    """Initializes Chrome WebDriver before a test and closes it afterward"""
    logger.info("=== Start test: %s ===", request.node.name)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    browser = webdriver.Chrome(options=options)
    browser.get(BASE_URL)

    yield browser

    logger.info("=== End test: %s ===\n", request.node.name)
    browser.quit()


@pytest.fixture
def authenticated(driver):
    """Logs in as the default test user and returns the authenticated driver"""
    logger.debug("Running 'authenticated' fixture setup")
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_login_form(DEFAULT_USER)
    login_page.click_on_login_button()

    # Fail fast if login failed during setup
    assert login_page.is_sign_out_displayed(), "Failed to log in inside 'authenticated' fixture"

    return driver


@pytest.fixture
def ensure_min_contacts(authenticated):
    """Ensures at least one contact exists in the list before running removal tests"""
    contacts_page = ContactsPage(authenticated)
    contact_page = ContactPage(authenticated)

    if contacts_page.get_contact_cards_number() < 1:
        logger.debug("No contacts found; creating a precondition contact")
        contact_page.create_contact_steps(generate_contact())
        contacts_page.open_contacts_list()

    return authenticated
