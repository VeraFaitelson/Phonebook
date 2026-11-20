"""Page Object for the Contacts list, details view, editing, and deletion"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ContactsPage(BasePage):
    """Encapsulates locators and actions for managing existing contacts"""

    # Navigation & Contact Cards
    CONTACTS_LINK = (By.CSS_SELECTOR, "[href='/contacts']")
    CONTACTS_CARDS = (By.CLASS_NAME, "contact-item_card__2SOIM")

    # Detailed Card View & Action Buttons
    DETAILED_CARD_TITLE = (By.CSS_SELECTOR, ".contact-item-detailed_card__50dTS h2")
    DETAILS_CARD = (By.CLASS_NAME, "contact-item-detailed_card__50dTS")
    BUTTON_EDIT = (By.XPATH, "//button[contains(text(),'Edit')]")
    BUTTON_REMOVE = (By.XPATH, "//button[text()='Remove']")
    EDIT_SAVE_BUTTON = (By.XPATH, "//button[contains(text(),'Save')]")

    # Edit Mode Inputs
    EDIT_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Name']")
    EDIT_LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    EDIT_PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Phone']")
    EDIT_EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='email']")
    EDIT_ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='Address']")
    EDIT_DESCRIPTION_INPUT = (By.CSS_SELECTOR, "input[placeholder='desc']")

    @staticmethod
    def get_card_locator(phone: str):
        """Builds a dynamic XPath locator for a contact card by its phone number"""
        return By.XPATH, f"//h3[contains(text(),'{phone}')]"

    def open_contacts_list(self):
        """Navigates to the Contacts page and waits for contact cards to load"""
        self.click(self.CONTACTS_LINK)
        self.wait.until(EC.url_contains("/contacts"))
        self.wait.until(EC.visibility_of_element_located(self.CONTACTS_CARDS))

    def contact_cards_visible(self, phone: str) -> bool:
        """Checks if a contact card with the specified phone number is visible"""
        return self.is_visible(self.get_card_locator(phone))

    def open_contact_details_card(self, phone: str):
        """Clicks on a contact card by phone number to open its details"""
        self.click(self.get_card_locator(phone))

    def open_edit_mode(self):
        """Stores current card text and switches the contact details card into edit mode"""
        self._old_card_text = self.find(self.DETAILS_CARD).text
        self.click(self.BUTTON_EDIT)

    def set_edit_mode(self, locator, value: str):
        """Updates a specific input field while in edit mode"""
        self.fill(locator, value)

    def submit_edit(self):
        """Saves changes and waits until the edit form closes and card text updates"""
        self.click(self.EDIT_SAVE_BUTTON)
        self.wait.until(EC.invisibility_of_element_located(self.EDIT_SAVE_BUTTON))
        self.wait.until(lambda d: self.find(self.DETAILS_CARD).text != self._old_card_text)

    def contact_name(self) -> str:
        """Extracts the first name from the detailed card header"""
        card = self.find(self.DETAILED_CARD_TITLE)
        return card.text.split()[0]

    def contact_last_name(self) -> str:
        """Extracts the last name from the detailed card header"""
        card = self.find(self.DETAILED_CARD_TITLE)
        return card.text.split()[1]

    def contact_email(self) -> str:
        """Extracts the email address from the detailed card text"""
        card = self.find(self.DETAILS_CARD)
        return card.text.split()[3]

    def get_contact_cards_number(self) -> int:
        """Returns the current count of contact cards in the list"""
        return len(self.driver.find_elements(*self.CONTACTS_CARDS))

    def open_first_contact(self):
        """Clicks on the first visible contact card in the list"""
        cards = self.wait.until(EC.visibility_of_all_elements_located(self.CONTACTS_CARDS))
        cards[0].click()

    def remove_contact(self):
        """Clicks 'Remove' and waits until the card count decreases by one"""
        initial_count = self.get_contact_cards_number()
        self.click(self.BUTTON_REMOVE)
        self.wait.until(lambda d: self.get_contact_cards_number() < initial_count)

    def remove_all_contacts(self):
        """Iteratively opens and removes all contacts until the list is empty"""
        while self.get_contact_cards_number() > 0:
            self.open_first_contact()
            self.remove_contact()


