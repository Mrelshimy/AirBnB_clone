#!/usr/bin/env python3
"""
This module provides base model class for creating entities in your app.
Each instance of the BaseModel class represents
a unique entity with a unique identifier
timestamps indicating when it was created and last updated
and any other attributes specific to the subclass.

Classes:
    BaseModel: A base model class for creating entities.
"""

import uuid
import datetime
import models


class BaseModel:
    """
    A base model that provides common attributes and methods for all models.

    Attributes:
        id (str): A unique identifier for each instance.
        created_at (datetime): The timestamp of when object was created.
        updated_at (datetime): The timestamp of when object was last updated.

    Methods:
        __init__(self, *args, **kwargs): Initializes new instance of the class.
        __str__(self): Returns a string representation of the instance.
        save(self): Saves the current state of the instance to storage.
        to_dict(self): Converts the instance attributes to a dictionary.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Raises:
            ValueError: If the kwarg 'created_at' or
            'updated_at' is not a valid ISO format datetime string.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.fromisoformat(value)
                if key == '__class__':
                    continue
                else:
                    setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: A string representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Saves the current state of the instance to storage.
        """
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Converts the instance attributes to a dictionary.

        Returns:
            dict: A dictionary representation of the instance.
        """
        o_dict = self.__dict__.copy()
        o_dict['created_at'] = datetime.datetime.isoformat(self.created_at)
        o_dict['updated_at'] = datetime.datetime.isoformat(self.updated_at)
        o_dict['__class__'] = self.__class__.__name__
        return o_dict
