#!/usr/bin/python3
""" write a user class that inherits from basemodel """
from models.base_model import BaseModel


class User(BaseModel):
    """ user class basemodel is parent """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
