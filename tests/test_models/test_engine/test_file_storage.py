#!/usr/bin/python3

import unittest
import os
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.model = BaseModel()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_method(self):
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertEqual(len(all_objs), 0)

    def test_new_method(self):
        obj_id = self.model.id
        self.storage.new(self.model)
        all_objs = self.storage.all()
        self.assertIn("BaseModel.{}".format(obj_id), all_objs.keys())

    def test_save_method(self):
        obj_id = self.model.id
        self.model.name = "Test Model"
        self.storage.new(self.model)
        self.storage.save()
        
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        
        self.assertIn("BaseModel.{}".format(obj_id), all_objs.keys())
        self.assertEqual(all_objs["BaseModel.{}".format(obj_id)]['name'], "Test Model")

    def test_reload_method(self):
        obj_id = self.model.id
        self.model.name = "Test Model"
        self.storage.new(self.model)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()

        self.assertIn("BaseModel.{}".format(obj_id), all_objs.keys())
        self.assertEqual(all_objs["BaseModel.{}".format(obj_id)]['name'], "Test Model")

if __name__ == '__main__':
    unittest.main()

