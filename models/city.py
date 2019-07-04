#!/usr/bin/python3
""" write a city class that inherits from basemodel """
from models.base_model import BaseModel


class City(BaseModel):
    """ state class basemodel is parent """
    state_id = ""
    name = ""
