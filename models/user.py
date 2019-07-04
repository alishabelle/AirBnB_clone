#!/usr/bin/python3
""" This is a class called User that inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """ user class basemodel is parent """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
=======

    def __init__(self):
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
>>>>>>> f75dc79cc34dfc5963e05ef727d433ed8a4ba590
