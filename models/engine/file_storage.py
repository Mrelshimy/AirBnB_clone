#!/usr/bin/python3
import json
from models.base_model import BaseModel
""" File Storage Module """


class FileStorage:
	"""
	Class for handling storage operations on a JSON file.

	Attributes:
		__file_path (str): Path to the JSON file.
		__objects (dict): Dictionary to store objects.
	"""
	__file_path = "file.json"
	__objects = {}

	def __init__(self):
		"""
		Constructs a new FileStorage object.
		"""
		pass

	def all(self):
		"""
		Returns all stored objects.

		Returns:
			dict: All stored objects.
		"""
		return FileStorage.__objects

	def new(self, obj):
		"""
		Adds a new object to the storage.

		Args:
			obj (object): Object to be added.
		"""
		FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

	def save(self):
		"""
		Saves all objects to the JSON file.
		"""
		with open(FileStorage.__file_path, "w") as file:
			x = FileStorage.__objects
			dic_of_objects = {obj: x[obj].to_dict() for obj in x.keys()}
			json.dump(dic_of_objects, file)

	def reload(self):
		"""
		Reloads objects from the JSON file.
		"""
		try:
			with open(FileStorage.__file_path, "r") as file:
				js_obj = json.load(file)
				for obj in js_obj.values():
					name_of_cls = obj["__class__"]
					del obj["__class__"]
					self.new(eval(name_of_cls)(**obj))
		except :
			pass
