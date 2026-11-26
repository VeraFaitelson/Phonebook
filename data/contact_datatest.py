"""Test data sets for parameterized contact validation tests"""
import pytest
from faker import Faker

fake = Faker()

PHONE_ALERT_TEXT = "Phone not valid: Phone number must contain only digits! And length min 10, max 15!"
EMAIL_ALERT_TEXT = "Email not valid"

INVALID_CONTACT_FIELDS = [
    pytest.param("phone", "", PHONE_ALERT_TEXT, id="phone_is_empty"),
    pytest.param("phone", "1234", PHONE_ALERT_TEXT, id="phone_too_short"),
    pytest.param("phone", fake.numerify("#" * 28), PHONE_ALERT_TEXT, id="phone_too_long"),
    pytest.param("phone", "dhrhehehehehz", PHONE_ALERT_TEXT, id="phone_with_letters"),
    pytest.param("email", "wfwfwwt3t3tt3", EMAIL_ALERT_TEXT, id="email_without_at"),
    pytest.param("email", "testgmail.com", EMAIL_ALERT_TEXT, id="email_missing_at"),
]