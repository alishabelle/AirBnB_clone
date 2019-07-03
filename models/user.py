#!/usr/bin/python3
""" write a user class that inherits from basemodel """
from models.base_model import BaseModel


class User(BaseModel):
    """ user class basemodel is parent """

    def __init__(self):
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
