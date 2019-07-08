#!/usr/bin/python3
""" test module for basemodel class """


from models.base_model import BaseModel
from models.user import User
import unittest
import uuid
import os.path
import os
import datetime


class test_base(unittest.TestCase):
    """ testing the basemodel class """

    def __init__(self, *args, **wouldbekwargs):
        """ instantiation of instance """

        super().__init__(*args, **wouldbekwargs)
        self._name = "BaseModel"
        self._class = BaseModel

    def test_timecreate(self):
        """ test for time creation """

        new_jawn = self._class()
        time = datetime.datetime.now()
        self.assertIsInstance(new_jawn.create_at, datetime.datetime)
        self.assertTrue(0 < (time - new_jawn.create_at).total_seconds() < 1)
