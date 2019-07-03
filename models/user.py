#!/usr/bin/python3
""" write a user class that inherits from basemodel """
from models.base_model import BaseModel


class User(BaseModel):
    """ user class basemodel is parent """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ ititializing these user class """
        super().__init__(self, *args, **kwargs)
