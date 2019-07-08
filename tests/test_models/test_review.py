#!/usr/bin/python3
""" test module for review class """

from models.base_model import BaseModel
from models.user import User
import unittest


class test_review(unittest.TestCase):
    """ testing the review class """

    def test_string(self):
        """ tests that the attributes name is a string """

        new_jawn = Review()
        text = getattr(new_jawn, "text")
        self.asserIsInstance(text, str)

    def test_string1(self):
        """ tests that the attributes name is a string """

        new_jawn = Review()
        place = getattr(new_jawn, "place_id")
        self.asserIsInstance(place, str)

    def test_string1(self):
        """ tests that the attributes name is a string """

        new_jawn = Review()
        user = getattr(new_jawn, "user_id")
        self.asserIsInstance(user, str)

    def test_inherit(self):
        """ tests review class inherits from basemodel """

        new_jawn = Review()
        self.assertIsInstance(new_jawn, BaseModel)

    def test_attribute(self):
        """ tests the class name attribute of city """

        new_jawn = Review()
        self.assertTrue("text" in new_jawn.__dir__())
        self.assertTrue("place_id" in new_jawn.__dir__())
        self.assertTrue("user_id" in new_jawn.__dir__())
