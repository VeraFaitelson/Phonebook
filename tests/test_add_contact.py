"""Tests for adding a new contact (positive and negative scenarios)"""
import pytest

from data.contact_datatest import INVALID_CONTACT_FIELDS
from pages.add_contact_page import ContactPage
from pages.contacts_page import ContactsPage
from utils.data_generator import generate_contact


def test_add_contact_with_all_fields_success(authenticated):
    """Verify successful creation of a contact when all fields are filled"""
    contact_page = ContactPage(authenticated)
    contacts_page = ContactsPage(authenticated)
    contact = generate_contact(with_description=True)

    contact_page.create_contact_steps(contact)

    assert contacts_page.contact_cards_visible(contact.phone)


def test_add_contact_without_description_success(authenticated):
    """Verify successful creation of a contact when optional description is omitted"""
    contact_page = ContactPage(authenticated)
    contacts_page = ContactsPage(authenticated)
    contact = generate_contact(with_description=False)

    contact_page.create_contact_steps(contact)

    assert contacts_page.contact_cards_visible(contact.phone)


@pytest.mark.parametrize("empty_field", ["name", "last_name", "address"])
def test_negative_add_contact_with_empty_required_field(authenticated, empty_field):
    """Verify contact is not saved when a required text field is left empty"""
    contact_page = ContactPage(authenticated)
    contact = generate_contact()
    setattr(contact, empty_field, "")

    contact_page.create_contact_steps(contact)

    assert contact_page.contact_save_button_visible()


@pytest.mark.parametrize("field_name, invalid_value, expected_alert", INVALID_CONTACT_FIELDS)
def test_negative_add_contact_with_invalid_fields(authenticated, field_name, invalid_value, expected_alert):
    """Verify validation alert appears when adding a contact with invalid phone or email"""
    contact_page = ContactPage(authenticated)
    contact = generate_contact()
    setattr(contact, field_name, invalid_value)

    contact_page.create_contact_steps(contact)

    alert_text = contact_page.get_alert_text()
    assert expected_alert in alert_text
    contact_page.accept_alert()
