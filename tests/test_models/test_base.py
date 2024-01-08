#!/usr/bin/python3
"""Testing BaseModel class module"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel



class TestBaseModemClass(unittest.TestCase):
	"""Testing BaseModem Class"""

	def setUp(self):
		self.model_1 = BaseModel()
		self.model_2 = BaseModel()

	def tearDown(self):
		del(self.model_1)
		del(self.model_2)

	def test_instance(self):
		"""Test Instance creation"""
		self.assertIsInstance(self.model_1, BaseModel)
		self.assertIsInstance(self.model_2, BaseModel)
		self.assertNotEqual(self.model_1, self.model_2)

	def test_id(self):
		"""Test id assignement"""
		self.assertEqual(type(self.model_1.id), str)
		self.assertTrue(hasattr(self.model_1, "id"))
		self.assertTrue(hasattr(self.model_2, "id"))
		self.assertNotEqual(self.model_1.id, self.model_2.id)

	def test_created_at(self):
		"""Test created_at attribute"""
		self.assertEqual(type(self.model_1.created_at), datetime)
		self.assertTrue(hasattr(self.model_1, "created_at"))
		self.assertTrue(hasattr(self.model_2, "created_at"))
	
	def test_update_at(self):
		"""Test updated_at attribute"""
		self.assertTrue(hasattr(self.model_1, "updated_at"))
		self.model_1.save()
		self.assertEqual(type(self.model_1.updated_at), datetime)
		self.assertNotEqual(self.model_1.created_at, self.model_1.updated_at)
	
	def test_to_dict(self):
		"""Test to_dict method"""
		O_dict = self.model_1.to_dict()
		self.assertIsInstance(O_dict, dict)
		self.assertTrue(O_dict['__class__'], BaseModel)
