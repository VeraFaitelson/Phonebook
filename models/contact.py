"""Contact data model"""

from dataclasses import dataclass


@dataclass
class Contact:
    """
    Data model representing a contact entity
    @dataclass generates utility methods:
    - __init__ (initialization of fields)
    - __repr__ (string representation of an object)
    - __eq__ (comparison of objects based on the values of their fields)
    """
    name: str
    last_name: str
    phone: str
    email: str
    address: str
    description: str = "" # Optional field; defaults to empty string if omitted