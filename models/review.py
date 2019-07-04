#!/usr/bin/python3
""" write a review class that inherits from basemodel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ review class basemodel is parent """

    def __init__(self):
        self.place_id = ''
        self.user_id = ''
        self.text = ''
