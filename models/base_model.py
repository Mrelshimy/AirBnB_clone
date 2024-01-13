#!/usr/bin/env python3
""" Base Model Class Module"""
import uuid
from datetime import datetime
# import models


class BaseModel:
    """Base Model Class"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        # if kwargs and len(kwargs) > 0:
        #     for key, value in kwargs.items():
        #         if key == 'created_at' or key == 'updated_at':
        #             value = datetime.fromisoformat(value)
        #         elif key == '__class__':
        #             continue
        #         else:
        #             setattr(self, key, value)
        # else:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
            # models.storage.new(self)

    def __str__(self):
        """Return String representation of an object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update Updated_at to current datetime"""
        self.updated_at = datetime.now()
        # models.storage.save()

    def to_dict(self):
        """Return a Dictionary representation of an object"""
        o_dict = self.__dict__.copy()
        o_dict['created_at'] = datetime.isoformat(self.created_at)
        o_dict['updated_at'] = datetime.isoformat(self.updated_at)
        o_dict['__class__'] = self.__class__.__name__
        return o_dict
