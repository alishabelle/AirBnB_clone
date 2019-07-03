#!/usr/bin/python3
""" write a user class that inherits from basemodel """
from models.base_model import BaseModel


class User(BaseModel):
    """ user class basemodel is parent """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **wouldbekwargs):
        """ ititializing these user class """
        if (wouldbekwargs.get('id') is not None):
            self.__dict__ = wouldbekwargs
        else:
            super().__init__(self)
