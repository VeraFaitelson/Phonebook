"""Tests for removing contacts from the list"""

from pages.add_contact_page import ContactPage
from pages.contacts_page import ContactsPage
from utils.data_generator import generate_contact

def test_remove_single_contact(authenticated):
    """Verify removing a single newly created contact decreases the list count by one"""
    contact_page = ContactPage(authenticated)
    contacts_page = ContactsPage(authenticated)
    contact = generate_contact()

    # Create a new contact so we have a guaranteed target to delete
    contact_page.create_contact_steps(contact)
    contacts_page.open_contacts_list()
    initial_count = contacts_page.get_contact_cards_number()

    # Open the newly created contact by its phone number and remove it
    contacts_page.open_contact_details_card(contact.phone)
    contacts_page.remove_contact()

    assert contacts_page.get_contact_cards_number() == initial_count - 1


def test_remove_all_contacts(authenticated):
    """Verify removing all contacts leaves the contacts list empty"""
    contact_page = ContactPage(authenticated)
    contacts_page = ContactsPage(authenticated)

    # Ensure at least one contact exists before clearing the list
    contact_page.create_contact_steps(generate_contact())
    contacts_page.open_contacts_list()
    contacts_page.remove_all_contacts()

    assert contacts_page.get_contact_cards_number() == 0
