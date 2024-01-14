#!/usr/bin/python3
"""Testing City class module"""
import unittest
import uuid
from datetime import datetime
from models.city import City
import os
from time import sleep


class TestBaseModemClass(unittest.TestCase):
    """Testing BaseModem Class"""

    def setUp(self):
        self.model_1 = City()
        self.model_2 = City()

    def tearDown(self):
        del self.model_1
        del self.model_2
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance(self):
        """Test Instance creation"""
        self.assertIsInstance(self.model_1, City)
        self.assertIsInstance(self.model_2, City)
        self.assertNotEqual(self.model_1, self.model_2)

    def test_id(self):
        """Test id assignement"""
        self.assertIsInstance(uuid.UUID(self.model_1.id), uuid.UUID)
        self.assertEqual(type(self.model_1.id), str)
        self.assertTrue(hasattr(self.model_1, "id"))
        self.assertTrue(hasattr(self.model_2, "id"))
        self.assertNotEqual(self.model_1.id, self.model_2.id)

    def test_created_at(self):
        """Test created_at attribute"""
        self.assertIsInstance(self.model_1.created_at, datetime)
        self.assertTrue(hasattr(self.model_1, "created_at"))
        self.assertTrue(hasattr(self.model_2, "created_at"))
        old = self.model_1.created_at
        sleep(0.05)
        b = City()
        self.model_1.save()
        self.assertEqual(old, self.model_1.created_at)
        self.assertNotEqual(b.created_at, self.model_1.created_at)

    def test_update_at(self):
        """Test updated_at attribute"""
        self.assertTrue(hasattr(self.model_1, "updated_at"))
        old = self.model_1.updated_at
        sleep(0.05)
        self.model_1.save()
        self.assertEqual(type(self.model_1.updated_at), datetime)
        self.assertLess(self.model_1.created_at,
                        self.model_1.updated_at)
        self.assertLess(old, self.model_1.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        O_dict = self.model_1.to_dict()
        self.assertIsInstance(O_dict, dict)
        self.assertTrue(O_dict['__class__'], City)
        self.assertEqual(O_dict['updated_at'],
                         datetime.isoformat(self.model_1.updated_at))
        self.assertEqual(O_dict['created_at'],
                         datetime.isoformat(self.model_1.created_at))

    def test_str(self):
        """Test __str__ method"""
        self.model_1.id = "abcd"
        result = f"[City] (abcd)"
        self.assertIn(result, self.model_1.__str__())
        self.assertIsInstance(self.model_1.__str__(), str)

    def test_name(self):
        """Test name attribute"""
        self.assertTrue(hasattr(self.model_1, "name"))
        self.assertIsInstance(self.model_1.name, str)

    def test_state_id(self):
        """Test state_id attribute"""
        self.assertTrue(hasattr(self.model_1, "state_id"))
        self.assertIsInstance(self.model_1.state_id, str)


if __name__ == "__main__":
    unittest.main()
