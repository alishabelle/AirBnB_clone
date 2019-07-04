#!/usr/bin/python3
""" write a review class that inherits from basemodel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ review class basemodel is parent """
    place_id = ""
    user_id = ""
    text = ""
