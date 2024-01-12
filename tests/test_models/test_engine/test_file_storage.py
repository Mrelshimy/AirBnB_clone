#!/usr/bin/python3
"""Testing File Storage Module"""
import models
import unittest
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def setUp(self):
        self.s1 = FileStorage()

    def tearDown(self):
        del self.s1
        if os.path.exists("file.json"):
            os.remove("file.json")

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
        bm = BaseModel()
        us = User()
        am = Amenity()
        ci = City()
        pl = Place()
        rv = Review()
        st = State()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(am)
        models.storage.new(ci)
        models.storage.new(pl)
        models.storage.new(rv)
        models.storage.new(st)
        models.storage.save()
        self.assertTrue(os.path.exists('file.json'))
        json_text = ""
        with open("file.json", "r") as file:
            json_text = file.read()
            self.assertIn("BaseModel." + bm.id, json_text)
            self.assertIn("User." + us.id, json_text)
            self.assertIn("Amenity." + am.id, json_text)
            self.assertIn("City." + ci.id, json_text)
            self.assertIn("Place." + pl.id, json_text)
            self.assertIn("Review." + rv.id, json_text)
            self.assertIn("State." + st.id, json_text)

        with self.assertRaises(TypeError):
            models.storage.save(None)
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_storage_reload_func(self):
        bm = BaseModel()
        us = User()
        am = Amenity()
        ci = City()
        pl = Place()
        rv = Review()
        st = State()
        self.s1.new(bm)
        self.s1.new(us)
        self.s1.new(am)
        self.s1.new(ci)
        self.s1.new(pl)
        self.s1.new(rv)
        self.s1.new(st)
        models.storage.save()
        self.assertTrue(os.path.exists('file.json'))
        self.s1.reload()
        objs = self.s1._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("City." + ci.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("Review." + rv.id, objs)
        self.assertIn("State." + st.id, objs)
        with self.assertRaises(TypeError):
            models.storage.reload(None)
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.assertIsNone(models.storage.reload())

    def test_json_file(self):
        with open("file.json", "w") as file:
            pass
        with self.assertRaises(json.decoder.JSONDecodeError):
            models.storage.reload()
        with open("file.json", "w") as file:
            file.write("{\"abcd\":\"12334\"}")
        with self.assertRaises(TypeError):
            models.storage.reload()
        with open("file.json", "w") as file:
            file.write("{}")


if __name__ == "__main__":
    unittest.main()
