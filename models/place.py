""" Place Class Module"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    The Place class inherits from the BaseModel class.
    It represents a place with attributes for
    city_id, user_id, name, description, number_rooms, number_bathrooms,
    max_guest, price_by_night, latitude, longitude, and amenity_ids.

    Attributes:
        city_id (str): ID of the city where the place is located.
        user_id (str): ID of the user who owns the place.
        name (str): name of the place.
        description (str): description of the place.
        number_rooms (int): number of rooms in the place.
        number_bathrooms (int): number of bathrooms in the place.
        max_guest (int): maximum number of guests allowed in the place.
        price_by_night (float): price per night for staying in the place.
        latitude (float): latitude coordinate of the place.
        longitude (float): longitude coordinate of the place.
        amenity_ids (list): list of IDs of amenities available in the place.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []


    def __init__(self):
        """
        Constructor for the Place class.
        """
        pass