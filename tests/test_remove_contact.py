"""Tests for removing contacts from the list"""
import logging

from pages.add_contact_page import ContactPage
from pages.contacts_page import ContactsPage

logger = logging.getLogger(__name__)

def test_remove_single_contact(ensure_min_contacts):
    """Verify removing a single contact decreases the list count by one"""
    contacts_page = ContactsPage(ensure_min_contacts)

    contacts_page.open_contacts_list()
    initial_count = contacts_page.get_contact_cards_number()

    contacts_page.open_first_contact()
    contacts_page.remove_contact()

    assert contacts_page.get_contact_cards_number() == initial_count - 1


def test_remove_all_contacts(ensure_min_contacts):
    """Verify removing all contacts leaves the contacts list empty"""
    contacts_page = ContactsPage(ensure_min_contacts)

    contacts_page.open_contacts_list()
    contacts_page.remove_all_contacts()

    assert contacts_page.get_contact_cards_number() == 0
