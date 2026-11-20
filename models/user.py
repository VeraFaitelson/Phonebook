"""User data model for authorization and registration"""

from dataclasses import dataclass


@dataclass
class User:
    """
    Data model representing a user entity
    @dataclass generates utility methods:
    - __init__ (initialization of fields)
    - __repr__ (string representation of an object)
    - __eq__ (comparison of objects based on the values of their fields)
    """
    email: str
    password: str