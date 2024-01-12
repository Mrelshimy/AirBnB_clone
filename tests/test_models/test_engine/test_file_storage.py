#!/usr/bin/python3
"""Testing File Storage Module"""
import models
import unittest
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def setUp(self):
        self.s1 = FileStorage()
    def test_FileStorage_instantiation(self):
        self.assertIsInstance(self.s1, FileStorage)
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_attr_type(self):
        self.assertIsInstance(self.s1._FileStorage__file_path, str)
        with self.assertRaises(AttributeError):
            self.s1.__file_path
        self.assertIsInstance(self.s1._FileStorage__objects, dict)
        with self.assertRaises(AttributeError):
            self.s1.__objects

    def test_storage_type(self):
        self.assertIsInstance(models.storage, FileStorage)

    def test_storage_all_func(self):
        self.assertEqual(dict, type(models.storage.all()))
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_storage_new_func(self):
        bm = BaseModel()
        us = User()
        am = Amenity()
        ci = City()
        pl = Place()
        rv = Review()
        st = State()
        models.storage.new(bm)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        models.storage.new(us)
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        models.storage.new(am)
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        models.storage.new(ci)
        self.assertIn("City." + ci.id, models.storage.all().keys())
        self.assertIn(ci, models.storage.all().values())
        models.storage.new(pl)
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        models.storage.new(rv)
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())
        models.storage.new(st)
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

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
