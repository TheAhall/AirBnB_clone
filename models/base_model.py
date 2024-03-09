#!/usr/bin/python3
"""
BaseModel - Module
"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """
    BaseModel class that defines common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute 'updated_at' with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        Includes the '__class__' attribute with the class name.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    @classmethod
    def from_dict(cls, obj_dict):
        """
        Creates a new instance of BaseModel from a dictionary representation.
        Args:
            obj_dict: A dictionary representing the BaseModel instance.
        Returns:
            A new instance of BaseModel.
        """
        if obj_dict is None or len(obj_dict) == 0:
            return cls()

        for key, value in obj_dict.items():
            if key == 'created_at' or key == 'updated_at':
                obj_dict[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

        return cls(**obj_dict)
