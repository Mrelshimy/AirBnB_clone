#!/usr/bin/python3
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[obj.__class__.__name__.id] = obj

    def save(self):
        with open(FileStorage.__file_path, "w") as file:
            x = json.dump(FileStorage.__objects, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as file:
                x = json.load(file)
                self.new(file)
        except:
            pass
