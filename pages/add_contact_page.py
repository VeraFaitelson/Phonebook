"""Page Object for the Add Contact form"""

from selenium.webdriver.common.by import By

from models.contact import Contact
from pages.base_page import BasePage


class ContactPage(BasePage):
    """Encapsulates locators and actions for creating a new contact"""

    # Locators
    ADD_CONTACT_BUTTON = (By.CSS_SELECTOR, "[href='/add']")
    NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Phone']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='email']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='Address']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "input[placeholder='description']")
    SAVE_BUTTON = (By.XPATH, "//button[contains(., 'Save')]")

    def open_contact_form(self):
        """Navigates to the Add Contact tab"""
        self.click(self.ADD_CONTACT_BUTTON)

    def fill_name(self, name: str):
        """Enters first name into the Name field"""
        self.fill(self.NAME_INPUT, name)

    def fill_last_name(self, last_name: str):
        """Enters last name into the Last Name field"""
        self.fill(self.LAST_NAME_INPUT, last_name)

    def fill_phone(self, phone: str):
        """Enters phone number into the Phone field"""
        self.fill(self.PHONE_INPUT, phone)

    def fill_email(self, email: str):
        """Enters email address into the Email field"""
        self.fill(self.EMAIL_INPUT, email)

    def fill_address(self, address: str):
        """Enters street/city address into the Address field"""
        self.fill(self.ADDRESS_INPUT, address)

    def fill_description(self, description: str):
        """Enters optional notes into the Description field"""
        self.fill(self.DESCRIPTION_INPUT, description)

    def fill_contact(self, contact: Contact):
        """Fills all contact form fields using a Contact model"""
        self.fill_name(contact.name)
        self.fill_last_name(contact.last_name)
        self.fill_phone(contact.phone)
        self.fill_email(contact.email)
        self.fill_address(contact.address)
        self.fill_description(contact.description)

    def submit_contact(self):
        """Clicks the Save button to submit the contact form"""
        self.click(self.SAVE_BUTTON)

    def create_contact_steps(self, contact: Contact):
        """Full workflow: opens the form, fills all fields, and saves the contact"""
        self.open_contact_form()
        self.fill_contact(contact)
        self.submit_contact()

    def contact_card_visible(self, phone: str) -> bool:
        """Checks if a contact card with the given phone number appears in the list"""
        locator = (By.XPATH, f"//h3[contains(text(),'{phone}')]")
        return self.is_visible(locator)

    def contact_save_button_visible(self) -> bool:
        """Checks if the contact Save button is still visible on the form."""
        return self.is_visible(self.SAVE_BUTTON)