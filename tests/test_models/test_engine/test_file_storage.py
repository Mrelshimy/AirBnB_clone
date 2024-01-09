#!/usr/bin/python3
"""Testing File Storage Module"""
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation(self):
        self.assertEqual(type(FileStorage()), FileStorage)
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_attr_type(self):
        self.assertEqual(str, type(FileStorage()._FileStorage__file_path))
        with self.assertRaises(AttributeError):
            FileStorage().__file_path
        self.assertEqual(dict, type(FileStorage()._FileStorage__objects))
        with self.assertRaises(AttributeError):
            FileStorage().__objects

    def test_storage_type(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_storage_all_func(self):
        self.assertEqual(dict, type(models.storage.all()))
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_storage_new_func(self):
        bm = models.base_model.BaseModel()
        models.storage.new(bm)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        with self.assertRaises(TypeError):
            models.storage.new(models.base_model.BaseModel(), 1)

    def test_storage_save_func(self):
        bm = models.base_model.BaseModel()
        models.storage.new(bm)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_storage_reload_func(self):
        bm = models.base_model.BaseModel()
        models.storage.new(bm)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage()._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
