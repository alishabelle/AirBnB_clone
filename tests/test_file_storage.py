#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import os


class Test_FileStorage(unittest.TestCase):

    def test1(self):
        """ Test to check if an object was created and stored
        """
        all_objs = storage.all()
        x = len(all_objs)
        model_one = BaseModel()
        model_one.save()
        self.assertNotEqual(x, len(storage.all()))

    def test2(self):
        """ Test tp check that all() method returns a dict """
        instance = FileStorage()
        self.assertEqual(dict, type(instance.all()))

    def test3(self):
        model_one = BaseModel()
        model_one.save()
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
