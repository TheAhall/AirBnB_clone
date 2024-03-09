#!/usr/bin/python3


import unittest
from models.base_model import BaseModel
from models.city import City


class TestUser(unittest.TestCase):

    def test_City_inheritance(self):
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)

    def test_User_attributes(self):
        new_city = City()
        self.assertTrue("state_id" in new_city.__dir__())
        self.assertTrue("name" in new_city.__dir__())

    def test_type_name(self):
        new_city = City()
        name = getattr(new_city, "name")
        self.assertIsInstance(name, str)

    def test_type_name(self):
        new_city = City()
        name = getattr(new_city, "state_id")
        self.assertIsInstance(name, str)
