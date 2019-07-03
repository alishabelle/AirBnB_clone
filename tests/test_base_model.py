#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):

    def test1(self):
        """ Test to check if uuid generated is of the class str """
        model_one = BaseModel()
        self.assertEqual(type(model_one.id), str)

    def test2(self):
        """ Test to check if two objects of the class BaseModel
        possess unique uuids
        """
        model_one = BaseModel()
        model_two = BaseModel()
        self.assertNotEqual(model_one.id, model_two.id)

    def test3(self):
        """ Test to check if created_at attribute is correctly
        displayed. Compares the time between two model objects in
        microseconds.
        """
        model_one = BaseModel()
        model_two = BaseModel()
        x = (model_two.created_at - model_one.created_at)
        x = x.microseconds
        self.assertLess(x, 200000)

    def test4(self):
        """ Test to check if save() method updates the updated_at attribute """
        model_one = BaseModel()
        x = model_one.updated_at
        model_one.save()
        y = model_one.updated_at
        self.assertNotEqual(x, y)

    def test5(self):
        """ Test to check if __str__ override is a string """
        model_one = BaseModel()
        self.assertEqual(type(model_one.__str__()), str)

    def test6(self):
        """ Test to check if to_dict() method is correct """
        model_one = BaseModel()
        x = model_one.__dict__.get('created_at').isoformat()
        y = model_one.__dict__.get('updated_at').isoformat()
        a_dict = {'__class__': 'BaseModel', 'id': '{}'.format(model_one.id),
                  'created_at': '{}'.format(x), 'updated_at': '{}'.format(y)}
        self.assertEqual(model_one.to_dict(), a_dict)

    def test7(self):
        """ Test to check if class name was added to the dict """
        model_one = BaseModel()
        self.assertNotIn('__class__', model_one.__dict__)
        a_dict = model_one.to_dict()
        self.assertIn('__class__', a_dict)

    def test8(self):
        """ Test to check if created_at and updated_at attributes were
        converted to strings in isoformat
        """
        model_one = BaseModel()
        x = model_one.__dict__.get('created_at')
        y = model_one.__dict__.get('updated_at')
        self.assertNotEqual(type(x), str)
        self.assertNotEqual(type(y), str)
        a_dict = model_one.to_dict()
        x = a_dict.get('created_at')
        y = a_dict.get('updated_at')
        self.assertEqual(type(x), str)
        self.assertEqual(type(y), str)

    def test9(self):
        """ Test to check if kwargs attributes were set properly """
        model_one = BaseModel(None, a=1, b=[1, 2, 3], c=(98, 98))
        self.assertEqual(model_one.a, 1)
        self.assertEqual(type(model_one.a), int)
        self.assertEqual(model_one.b, [1, 2, 3])
        self.assertEqual(type(model_one.b), list)
        self.assertEqual(model_one.c, (98, 98))
        self.assertEqual(type(model_one.c), tuple)

    def test10(self):
        """ Test to check if None is passed to kwargs, then attributes
        are still set appropriately
        """
        model_one = BaseModel(None, None)
        self.assertIsNotNone(model_one.id)
        self.assertIsNotNone(model_one.created_at)
        self.assertIsNotNone(model_one.updated_at)
