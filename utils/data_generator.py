"""Test data generation helpers using Faker and UUID"""

import uuid
from faker import Faker

from models.contact import Contact

fake = Faker()


def generate_unique_email() -> str:
    """Generates a unique email address for registration tests"""
    return f"testQA_{uuid.uuid4().hex[:8]}@gmail.com"


def generate_contact(with_description: bool = True) -> Contact:
    """Creates a Contact object with random valid test data"""
    description = fake.sentence(nb_words=4) if with_description else ""

    return Contact(
        name=fake.first_name(),
        last_name=fake.last_name(),
        phone=fake.numerify("05########"),
        email=fake.unique.email(),
        address=fake.address(),
        description=description,
    )
