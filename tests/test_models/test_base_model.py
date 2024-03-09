#!/usr/bin/python3

"""
    the tests for base_model
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_create_instance(self):
        self.assertTrue(isinstance(self.model, BaseModel))

    def test_attributes(self):
        self.model.name = "Test"
        self.assertEqual(self.model.name, "Test")

    def test_save_method(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        expected_dict = {
            'id': str(self.model.id),
            'created_at': self.model.created_at.isoformat(),
            'updated_at': self.model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertEqual(self.model.to_dict(), expected_dict)

    def test_from_dict_method(self):
        data = {
            'id': '1234',
            'created_at': '2022-01-01T12:00:00',
            'updated_at': '2022-01-02T12:00:00',
            '__class__': 'BaseModel'
        }
        new_model = BaseModel(**data)
        self.assertEqual(new_model.id, '1234')
        self.assertEqual(new_model.created_at, datetime(2022, 1, 1, 12, 0, 0))
        self.assertEqual(new_model.updated_at, datetime(2022, 1, 2, 12, 0, 0))

if __name__ == '__main__':
    unittest.main()
