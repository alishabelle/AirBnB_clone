#!/usr/bin/python3
""" test module for amenity class """

from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class test_amenity(unittest.TestCase):
    """ testing the amenity class """

    def test_string(self):
        """ tests that the attributes name is a string """

        new_jawn = Amenity()
        name = getattr(new_jawn, "name")
        self.assertIsInstance(name, str)

    def test_inherit(self):
        """ tests amenity class inherits from basemodel """

        new_jawn = Amenity()
        self.assertIsInstance(new_jawn, BaseModel)

    def test_attribute(self):
        """ tests the class name attribute of amenity """

        new_jawn = Amenity()
        self.assertTrue("name" in new_jawn.__dir__())
