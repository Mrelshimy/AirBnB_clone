#!/usr/bin/python3
"""Testing Amenity class module"""
import os
import unittest
from models import storage
import uuid
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
import sys


class TestConsole(unittest.TestCase):
    """Testing BaseModem Class"""

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_prompt(self):
        self.assertEqual(HBNBCommand.prompt, "(hbnb) ")

    def test_do_quit(self):
        with patch("sys.stdout", new=StringIO()):
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_do_EOF(self):
        with patch("sys.stdout", new=StringIO()):
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_emptyline(self):
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().emptyline()
            self.assertEqual(otpt.getvalue(), "")

    def test_create(self):
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create BaseModel")
            class_id = f"{otpt.getvalue().strip()}"
            self.assertIsInstance(uuid.UUID(class_id), uuid.UUID)
            thekey = f"BaseModel.{class_id}"
            self.assertIn(thekey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create City")
            class_id = f"{otpt.getvalue().strip()}"
            self.assertIsInstance(uuid.UUID(class_id), uuid.UUID)
            thekey = f"City.{class_id}"
            self.assertIn(thekey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create Place")
            class_id = f"{otpt.getvalue().strip()}"
            self.assertIsInstance(uuid.UUID(class_id), uuid.UUID)
            thekey = f"Place.{class_id}"
            self.assertIn(thekey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create User")
            class_id = f"{otpt.getvalue().strip()}"
            self.assertIsInstance(uuid.UUID(class_id), uuid.UUID)
            thekey = f"User.{class_id}"
            self.assertIn(thekey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create State")
            class_id = f"{otpt.getvalue().strip()}"
            self.assertIsInstance(uuid.UUID(class_id), uuid.UUID)
            thekey = f"State.{class_id}"
            self.assertIn(thekey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create Review")
            class_id = f"{otpt.getvalue().strip()}"
            self.assertIsInstance(uuid.UUID(class_id), uuid.UUID)
            thekey = f"Review.{class_id}"
            self.assertIn(thekey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create Amenity")
            class_id = f"{otpt.getvalue().strip()}"
            self.assertIsInstance(uuid.UUID(class_id), uuid.UUID)
            thekey = f"Amenity.{class_id}"
            self.assertIn(thekey, storage.all().keys())

    def test_create_errors(self):
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create ")
            error_message = "** class name missing **"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create abcd")
            error_message = "** class doesn't exist **"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("User.create()")
            error_message = "*** Unknown syntax: User.create()"
            self.assertEqual(otpt.getvalue().strip(), error_message)

    def test_show(self):
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create BaseModel")
            class_id = f"{otpt.getvalue().strip()}"
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd(f"show BaseModel {class_id}")
            obj_str = storage.all()[f"BaseModel.{class_id}"].__str__()
            self.assertEqual(otpt.getvalue().strip(), obj_str)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd(f"BaseModel.show(\"{class_id}\")")
            obj_str = storage.all()[f"BaseModel.{class_id}"].__str__()
            self.assertEqual(otpt.getvalue().strip(), obj_str)

    def test_show_errors(self):
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("show ")
            error_message = "** class name missing **"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("show abcd")
            error_message = "** class doesn't exist **"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("show User")
            error_message = "** instance id missing **"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("show User 12434")
            error_message = "** no instance found **"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd(".User(\"1234\")")
            error_message = "*** Unknown syntax: .User(\"1234\")"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        # with patch("sys.stdout", new=StringIO()) as otpt:
        #     HBNBCommand().onecmd("show abcd")
        #     error_message = "** class doesn't exist **"
        #     self.assertEqual(otpt.getvalue().strip(), error_message)
        # with patch("sys.stdout", new=StringIO()) as otpt:
        #     HBNBCommand().onecmd("show User")
        #     error_message = "** instance id missing **"
        #     self.assertEqual(otpt.getvalue().strip(), error_message)
        # with patch("sys.stdout", new=StringIO()) as otpt:
        #     HBNBCommand().onecmd("show User 12434")
        #     error_message = "** no instance found **"
        #     self.assertEqual(otpt.getvalue().strip(), error_message)

if __name__ == "__main__":
    unittest.main()
