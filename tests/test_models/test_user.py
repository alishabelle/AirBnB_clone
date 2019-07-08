#!/usr/bin/python3
""" test module for user class """

from models.base_model import BaseModel
from models.user import User
import unittest


class test_user(unittest.TestCase):
    """ testing the user class """

    def test_string(self):
        """ tests that the attributes name is a string """

        new_jawn = User()
        first = getattr(new_jawn, "first_name")
        self.assertIsInstance(first, str)

    def test_string1(self):
        """ tests that the attributes name is a string """

        new_jawn = User()
        last = getattr(new_jawn, "last_name")
        self.assertIsInstance(last, str)

    def test_string2(self):
        """ test that the attributes name is a string """

        new_jawn = User()
        passwd = getattr(new_jawn, "password")
        self.assertIsInstance(passwd, str)

    def test_string3(self):
        """ tests that the attributes name is a string """

        new_jawn = User()
        email = getattr(new_jawn, "email")
        self.assertIsInstance(email, str)

    def test_inherit(self):
        """ tests user class inherits from basemodel """

        new_jawn = User()
        self.asserIsInstance(new_jawn, BaseModel)

    def test_attribute(self):
        """ tests the class name attribute of user """

        new_jawn = User()
        self.assertTrue("first_name", in new_jawn.__dir__())
        self.assertTrue("last_name", in new_jawn.__dir__())
        self.assertTrue("email", in new_jawn.__dir__())
        self.assertTrue("password", in new_jawn.__dir__())
