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
        new_dict = FileStorage.__objects.copy()
        with open(FileStorage.__file_path, "w") as write_file:
            for key, val in new_dict.items():
                if not isinstance(val, dict):
                    FileStorage.__objects[key] = val.to_dict()
            json.dump(FileStorage.__objects, write_file)

    def reload(self):
        import os.path
        from models.base_model import BaseModel
        from models.user import User
<<<<<<< HEAD
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        loads = {}
        new_dict = {}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as my_file:
                loads = json.load(my_file)
                for key, val in loads.items():
                    new_dict = val
                    if new_dict['__class__'] == 'BaseModel':
                        okay = BaseModel(None, **new_dict)
                    if new_dict['__class__'] == 'User':
                        okay = User(None, **new_dict)
                    if new_dict['__class__'] == 'State':
                        okay = State(None, **new_dict)  
                    if new_dict['__class__'] == 'City':
                        okay = City(None, **new_dict)  
                    if new_dict['__class__'] == 'Amenity':
                        okay = Amenity(None, **new_dict)  
                    if new_dict['__class__'] == 'Place':
                         okay = Place(None, **new_dict)  
                    if new_dict['__class__'] == 'Review':
                         okay = Review(None, **new_dict)  
                    loads[key] = okay
                FileStorage.__objects = loads
=======

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as my_file:
                FileStorage.__objects = json.load(my_file)
        for key, val in FileStorage.__objects.items():
            if 'BaseModel' in key:
                new_obj = BaseModel(None, **val)
            elif 'User' in key:
                new_obj = User(None, **val)
            FileStorage.__objects[key] = new_obj
>>>>>>> f75dc79cc34dfc5963e05ef727d433ed8a4ba590
