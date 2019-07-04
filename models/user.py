#!/usr/bin/python3
""" This is a class called User that inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ user class basemodel is parent """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
