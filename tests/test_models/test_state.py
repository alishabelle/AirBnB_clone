#!/usr/bin/python3
""" test module for state class """

from models.base_model import BaseModel
from models.user import User
import unittest


class test_state(unittest.TestCase):
    """ testing the state class """

    def test_string(self):
        """ tests that the attributes name is a string """

        new_jawn = State()
        name = getattr(new_jawn, "name")
        self.asserIsInstacne(name, str)

    def test_inherit(self):
        """ tests state class inherits from basemodel """

        new_jawn = State()
        self.assertIsInstance(new_jawn, BaseModel)

    def test_attribute(self):
        """ tests the class name attribute of user """

        new_jawn = State()
        self.assertTrue("name" in new_jawn.__dir__())
