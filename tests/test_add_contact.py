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

def test_negative_add_contact_with_invalid_telephone(authenticated):
    """Verify validation alert appears when adding a contact with an invalid phone number"""
    contact_page = ContactPage(authenticated)
    contact = generate_contact()
    contact.phone = "123"  # Invalid phone: shorter than 10 digits

    contact_page.open_contact_form()
    contact_page.fill_contact(contact)
    contact_page.submit_contact()

    alert_text = contact_page.get_alert_text()
    assert "Phone not valid" in alert_text
    contact_page.accept_alert()

def test_negative_add_contact_with_invalid_email(authenticated):
    """Verify validation alert appears when adding a contact with an invalid email"""
    contact_page = ContactPage(authenticated)
    contact = generate_contact()
    contact.email = "testgmail.com"  # Invalid email

    contact_page.open_contact_form()
    contact_page.fill_contact(contact)
    contact_page.submit_contact()

    alert_text = contact_page.get_alert_text()
    assert "Email not valid" in alert_text
    contact_page.accept_alert()

def test_negative_add_contact_with_empty_name(authenticated):
    """Verify contact is not saved when the required 'Name' field is empty"""
    contact_page = ContactPage(authenticated)
    contact = generate_contact()
    contact.name = ""  # Empty name

    contact_page.open_contact_form()
    contact_page.fill_contact(contact)
    contact_page.submit_contact()

    assert contact_page.contact_save_button_visible()

def test_negative_add_contact_with_empty_last_name(authenticated):
    """Verify contact is not saved when the required 'Last Name' field is empty"""
    contact_page = ContactPage(authenticated)
    contact = generate_contact()
    contact.last_name = ""  # Empty last name

    contact_page.open_contact_form()
    contact_page.fill_contact(contact)
    contact_page.submit_contact()

    assert contact_page.contact_save_button_visible()

def test_negative_add_contact_with_empty_address(authenticated):
    """Verify contact is not saved when the required 'Address' field is empty"""

    contact_page = ContactPage(authenticated)
    contact = generate_contact()
    contact.address = ""  # Empty address

    contact_page.open_contact_form()
    contact_page.fill_contact(contact)
    contact_page.submit_contact()

    assert contact_page.contact_save_button_visible()

