#!/usr/bin/python3
""" Amenity Class Module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    The Amenity class inherits from the BaseModel class.
    It represents an amenity with attributes for
    name.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""

    def __init__(self):
        """
        Constructor for the Amenity class.
        """
        pass
