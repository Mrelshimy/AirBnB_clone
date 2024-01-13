#!/usr/bin/python3
"""Testing Place class module"""
import unittest
import uuid
from datetime import datetime
from models.place import Place
import os


class TestBaseModemClass(unittest.TestCase):
    """Testing BaseModem Class"""

    def setUp(self):
        self.model_1 = Place()
        self.model_2 = Place()

    def tearDown(self):
        del self.model_1
        del self.model_2
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance(self):
        """Test Instance creation"""
        self.assertIsInstance(self.model_1, Place)
        self.assertIsInstance(self.model_2, Place)
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
        self.model_1.save()
        self.assertEqual(type(self.model_1.updated_at), datetime)
        self.assertNotEqual(self.model_1.created_at,
                            self.model_1.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        O_dict = self.model_1.to_dict()
        self.assertIsInstance(O_dict, dict)
        self.assertTrue(O_dict['__class__'], Place)
        self.assertEqual(O_dict['updated_at'],
                         datetime.isoformat(self.model_1.updated_at))
        self.assertEqual(O_dict['created_at'],
                         datetime.isoformat(self.model_1.created_at))

    def test_str(self):
        """Test __str__ method"""
        self.model_1.id = "abcd"
        result = f"[Place] (abcd)"
        self.assertIn(result, self.model_1.__str__())
        self.assertIsInstance(self.model_1.__str__(), str)

    def test_name(self):
        """Test name attribute"""
        self.assertTrue(hasattr(self.model_1, "name"))
        self.assertIsInstance(self.model_1.name, str)

    def test_city_id(self):
        """Test city_id attribute"""
        self.assertTrue(hasattr(self.model_1, "city_id"))
        self.assertIsInstance(self.model_1.city_id, str)

    def test_user_id(self):
        """Test user_id attribute"""
        self.assertTrue(hasattr(self.model_1, "user_id"))
        self.assertIsInstance(self.model_1.user_id, str)

    def test_description(self):
        """Test description attribute"""
        self.assertTrue(hasattr(self.model_1, "description"))
        self.assertIsInstance(self.model_1.description, str)

    def test_number_rooms(self):
        """Test number_rooms attribute"""
        self.assertTrue(hasattr(self.model_1, "number_rooms"))
        self.assertIsInstance(self.model_1.number_rooms, int)

    def test_number_bathrooms(self):
        """Test number_bathrooms attribute"""
        self.assertTrue(hasattr(self.model_1, "number_bathrooms"))
        self.assertIsInstance(self.model_1.number_bathrooms, int)

    def test_max_guest(self):
        """Test max_guest attribute"""
        self.assertTrue(hasattr(self.model_1, "max_guest"))
        self.assertIsInstance(self.model_1.max_guest, int)

    def test_price_by_night(self):
        """Test price_by_night attribute"""
        self.assertTrue(hasattr(self.model_1, "price_by_night"))
        self.assertIsInstance(self.model_1.price_by_night, int)

    def test_latitude(self):
        """Test latitude attribute"""
        self.assertTrue(hasattr(self.model_1, "latitude"))
        self.assertIsInstance(self.model_1.latitude, float)

    def test_longitude(self):
        """Test longitude attribute"""
        self.assertTrue(hasattr(self.model_1, "longitude"))
        self.assertIsInstance(self.model_1.longitude, float)

    def test_amenity_ids(self):
        """Test amenity_ids attribute"""
        self.assertTrue(hasattr(self.model_1, "amenity_ids"))
        self.assertIsInstance(self.model_1.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
