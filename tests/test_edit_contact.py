"""Tests for editing existing contact fields"""

import logging
import pytest

from pages.add_contact_page import ContactPage
from pages.contacts_page import ContactsPage
from utils.data_generator import fake, generate_contact

logger = logging.getLogger(__name__)

def test_edit_contact_name_field(authenticated):
    """Verify updating a contact's first name"""
    contact_page = ContactPage(authenticated)
    contacts_page = ContactsPage(authenticated)

    contact = generate_contact()
    contact_page.create_contact_steps(contact)
    new_name = fake.first_name()

    contacts_page.open_contact_details_card(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_mode(contacts_page.EDIT_NAME_INPUT, new_name)
    contacts_page.submit_edit()

    assert contacts_page.contact_name() == new_name


def test_edit_contact_last_name_field(authenticated):
    """Verify updating a contact's last name"""
    contact_page = ContactPage(authenticated)
    contacts_page = ContactsPage(authenticated)

    contact = generate_contact()
    contact_page.create_contact_steps(contact)
    new_last_name = fake.last_name()

    contacts_page.open_contact_details_card(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_mode(contacts_page.EDIT_LAST_NAME_INPUT, new_last_name)
    contacts_page.submit_edit()

    assert contacts_page.contact_last_name() == new_last_name


def test_edit_contact_phone_field(authenticated):
    """Verify updating a contact's phone number"""
    contact_page = ContactPage(authenticated)
    contacts_page = ContactsPage(authenticated)

    contact = generate_contact()
    contact_page.create_contact_steps(contact)
    new_phone = fake.numerify(text="050#######")

    logger.info("Updating contact phone: %s -> %s", contact.phone, new_phone)
    contacts_page.open_contact_details_card(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_mode(contacts_page.EDIT_PHONE_INPUT, new_phone)
    contacts_page.submit_edit()

    assert contacts_page.contact_cards_visible(new_phone)


def test_edit_contact_email_field(authenticated):
    """Verify updating a contact's email address"""
    contact_page = ContactPage(authenticated)
    contacts_page = ContactsPage(authenticated)

    contact = generate_contact()
    contact_page.create_contact_steps(contact)
    new_email = fake.unique.email()

    contacts_page.open_contact_details_card(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_mode(contacts_page.EDIT_EMAIL_INPUT, new_email)
    contacts_page.submit_edit()

    assert contacts_page.contact_email() == new_email

def test_edit_contact_address_field(authenticated):
    """Verify updating a contact's address"""
    contact_page = ContactPage(authenticated)
    contacts_page = ContactsPage(authenticated)

    contact = generate_contact()
    contact_page.create_contact_steps(contact)
    new_address = fake.street_address()

    contacts_page.open_contact_details_card(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_mode(contacts_page.EDIT_ADDRESS_INPUT, new_address)
    contacts_page.submit_edit()

    assert contacts_page.contact_address() == new_address

@pytest.mark.xfail(reason="Known UI bug: editing description displays 'Description: [object Undefined]'")
def test_edit_contact_description_field(authenticated):
    """Verify updating a contact's description"""
    contact_page = ContactPage(authenticated)
    contacts_page = ContactsPage(authenticated)

    contact = generate_contact()
    contact_page.create_contact_steps(contact)
    new_description = fake.sentence(nb_words=4)

    contacts_page.open_contact_details_card(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_mode(contacts_page.EDIT_DESCRIPTION_INPUT, new_description)
    contacts_page.submit_edit()

    assert contacts_page.contact_description() == new_description
