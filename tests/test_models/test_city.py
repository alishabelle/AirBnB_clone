#!/usr/bin/python3
""" test module for city class """

from models.base_model import BaseModel
from models.city import City
import unittest


class test_city(unittest.TestCase):
    """ testing the city class """

    def test_string(self):
        """ tests that the attributes name is a string """

        new_jawn = City()
        name = getattr(new_jawn, "name")
        self.assertIsInstance(name, str)

    def test_inherit(self):
        """ tests city class inherits from basemodel """

        new_jawn = City()
        self.assertIsInstance(new_jawn, BaseModel)

    def test_attribute(self):
        """ tests the class name attribute of city """

        new_jawn = City()
        self.assertTrue("state_id" in new_jawn.__dir__())
        self.asserTrue("name" in new_jawn.__dir__())
