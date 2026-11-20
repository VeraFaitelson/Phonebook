"""Tests for adding new contacts"""

from pages.add_contact_page import ContactPage
from utils.data_generator import generate_contact


def test_add_contact_success(authenticated):
    """Verify creating a contact with all fields populated"""
    contact_page = ContactPage(authenticated)
    contact = generate_contact(with_description=True)

    contact_page.open_contact_form()
    contact_page.fill_contact(contact)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)


def test_add_contact_only_required_fields(authenticated):
    """Verify creating a contact when optional 'description' field is left empty"""
    contact_page = ContactPage(authenticated)
    contact = generate_contact(with_description=False)

    contact_page.open_contact_form()
    contact_page.fill_contact(contact)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)
