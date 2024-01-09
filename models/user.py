#!/usr/bin/python3
""" User Class Module"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    The User class inherits from the BaseModel class.
    It represents a user with attributes for
    email, password, first name, and last name.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        """
        Constructor for the User class.
        """
        pass
