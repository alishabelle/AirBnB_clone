#!/usr/bin/python3
""" This is a class called User that inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):

    def __init__(self):
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
