#!/usr/bin/python3

"""
    Define class FileStorage Module
"""

import json
from models.base_model import BaseModel

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(json_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                json_dict = json.load(file)

            for key, value in json_dict.items():
                class_name, obj_id = key.split('.')
                obj = BaseModel.from_dict(value)
                self.__objects[key] = obj

        except FileNotFoundError:
            pass
