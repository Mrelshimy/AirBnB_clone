#!/usr/bin/python3
""" City Class Module"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    The City class inherits from the BaseModel class.
    It represents a city with attributes for
    name and state_id.

    Attributes:
        name (str): The name of the city.
        state_id (str): The ID of the state where the city is located.
    """

    name = ""
    state_id = ""
