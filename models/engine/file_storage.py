#!/usr/bin/python3
import json


class FileStorage:
    """ class used to store and retrieve stuff from json """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        for key, val in FileStorage.__objects.items():
            if not isinstance(val, dict):
                FileStorage.__objects[key] = val.to_dict()
        with open(FileStorage.__file_path, "w") as write_file:
            json.dump(FileStorage.__objects, write_file)

    def reload(self):
        import os.path
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        list_class = ["BaseModel", "Amenity", "City", "Place",
                      "Review", "State", "User"]

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as my_file:
                FileStorage.__objects = json.load(my_file)
                for key, val in FileStorage.__objects.items():
                    new_obj = FileStorage.__objects[key].get("__class__")
                    if new_obj in list_class:
                        class_fun = list_class.get(new_obj)
                        FileStorage.__objects[key] = class_fun(**FileStorage.
                                                               __objects[key])
