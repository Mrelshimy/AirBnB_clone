#!/usr/bin/python3
"""Testing User class module"""
import unittest
import uuid
from datetime import datetime
from models.user import User
import os
from time import sleep


class TestBaseModemClass(unittest.TestCase):
    """Testing BaseModem Class"""

    def setUp(self):
        self.model_1 = User()
        self.model_2 = User()

    def tearDown(self):
        del self.model_1
        del self.model_2
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance(self):
        """Test Instance creation"""
        self.assertIsInstance(self.model_1, User)
        self.assertIsInstance(self.model_2, User)
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

    def test_update_at(self):
        """Test updated_at attribute"""
        self.assertTrue(hasattr(self.model_1, "updated_at"))
        self.assertAlmostEqual(self.model_1.created_at,
                               self.model_1.updated_at)
        old_date = self.model_1.updated_at
        sleep(0.5)
        self.model_1.save()
        self.assertLess(old_date, self.model_1.updated_at)
        self.assertEqual(type(self.model_1.updated_at), datetime)
        self.assertNotEqual(self.model_1.created_at,
                            self.model_1.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        O_dict = self.model_1.to_dict()
        self.assertIsInstance(O_dict, dict)
        self.assertTrue(O_dict['__class__'], User)
        self.assertEqual(O_dict['updated_at'],
                         datetime.isoformat(self.model_1.updated_at))
        self.assertEqual(O_dict['created_at'],
                         datetime.isoformat(self.model_1.created_at))

    def test_str(self):
        """Test __str__ method"""
        self.model_1.id = "abcd"
        result = f"[User] (abcd)"
        self.assertIn(result, self.model_1.__str__())
        self.assertIsInstance(self.model_1.__str__(), str)

    def test_email(self):
        """Test email attribute"""
        self.assertTrue(hasattr(self.model_1, "email"))
        self.assertIsInstance(self.model_1.email, str)

    def test_password(self):
        """Test password attribute"""
        self.assertTrue(hasattr(self.model_1, "password"))
        self.assertIsInstance(self.model_1.password, str)

    def first_name(self):
        """Test first_name attribute"""
        self.assertTrue(hasattr(self.model_1, "first_name"))
        self.assertIsInstance(self.model_1.first_name, str)

    def last_name(self):
        """Test last_name attribute"""
        self.assertTrue(hasattr(self.model_1, "last_name"))
        self.assertIsInstance(self.model_1.last_name, str)


if __name__ == "__main__":
    unittest.main()
