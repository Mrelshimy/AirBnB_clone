#!/usr/bin/python3
import json
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
		FileStorage.__objects[obj.__class__.__name__.id] = obj

	def save(self):
		"""
		Saves all objects to the JSON file.
		"""
		with open(FileStorage.__file_path, "w") as file:
			x = json.dump(FileStorage.__objects, file)

	def reload(self):
		"""
		Reloads objects from the JSON file.
		"""
		try:
			with open(FileStorage.__file_path, "r") as file:
				x = json.load(file)
				self.new(file)
		except:
			pass
