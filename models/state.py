#!/usr/bin/python3
""" write a state class that inherits from basemodel """
from models.base_model import BaseModel


class State(BaseModel):
    """ user state basemodel is parent """
    name = ""
