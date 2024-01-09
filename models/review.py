#!/usr/bin/python3
""" Review Class Module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    The Review class inherits from the BaseModel class.
    It represents a review with attributes for
    place_id, user_id, and text.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self):
        """
        Constructor for the Review class.
        """
        pass
