#!/usr/bin/python3

import unittest
import os
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "file_test.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.model = BaseModel()
        self.model.name = "Test Model"
        self.model.my_number = 123
        self.model.save()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        all_objects = self.storage.all()
        self.assertIsNotNone(all_objects)
        self.assertIsInstance(all_objects, dict)
        self.assertIn("BaseModel.{}".format(self.model.id), all_objects)
        self.assertEqual(all_objects["BaseModel.{}".format(self.model.id)], self.model)

    def test_new(self):
        new_model = BaseModel()
        new_model.name = "New Test Model"
        new_model.my_number = 456
        self.assertNotIn("BaseModel.{}".format(new_model.id), self.storage.all())
        self.storage.new(new_model)
        self.assertIn("BaseModel.{}".format(new_model.id), self.storage.all())
        self.assertEqual(self.storage.all()["BaseModel.{}".format(new_model.id)], new_model)

    def test_save_reload(self):
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

        with open(self.file_path, 'r') as file:
            data = json.load(file)

        self.assertIn("BaseModel.{}".format(self.model.id), data)
        self.assertEqual(data["BaseModel.{}".format(self.model.id)]['name'], self.model.name)
        self.assertEqual(data["BaseModel.{}".format(self.model.id)]['my_number'], self.model.my_number)

        # Now let's reload the storage
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()
        reloaded_objects = new_storage.all()

        self.assertIn("BaseModel.{}".format(self.model.id), reloaded_objects)
        reloaded_model = reloaded_objects["BaseModel.{}".format(self.model.id)]
        self.assertIsInstance(reloaded_model, BaseModel)
        self.assertEqual(reloaded_model.id, self.model.id)
        self.assertEqual(reloaded_model.name, self.model.name)
        self.assertEqual(reloaded_model.my_number, self.model.my_number)


if __name__ == '__main__':
    unittest.main()
