#!/usr/bin/python3
import uuid
import datetime
from models import storage


class BaseModel:
    """ Class that serves as the base of the AirBnB project.

    Args:
        args: variable arguments
        kwargs: keyworded variable arguments

    Attributes:
        args: variable arguments
        kwargs keyworded variable arguments
    """

    def __init__(self, *args, **kwargs):
        """ Instantiation """
        if kwargs:  # Same thing as if len(kwargs) != 0
            for key, val, in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.datetime.strptime(val, "%Y-%m-\
%dT%H:%M:%S.%f"))
                else:
                    if key != '__class__':
                        setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """ Method to override __str__ """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ Method to update attribute updated_at """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ Method returns a dictionary representation of the class """
        a_dict = self.__dict__.copy()
        a_dict.update({'__class__': '{}'.format(
            self.__class__.__name__)})

        x = a_dict.get('created_at')
        if x is not None:
            x = x.isoformat()
            a_dict.update({'created_at': '{}'.format(x)})

        x = a_dict.get('updated_at')
        if x is not None:
            x = x.isoformat()
            a_dict.update({'updated_at': '{}'.format(x)})

        return a_dict
