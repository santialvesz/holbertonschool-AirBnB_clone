#!/usr/bin/python3


import uuid
from datetime import datetime
import models


class BaseModel():
    """
    Defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
         """
        This function is the constructor for the BaseModel class. It creates a new instance of the
        BaseModel class and assigns it an id, created_at, and updated_at
        """
        if len(kwargs) > 0:
            fmt = '%Y-%m-%dT%H:%M:%S.%f'
            for i, j in kwargs.items():
                if i == 'created_at':
                    self.created_at = datetime.fromisoformat(j)
                if i == 'updated_at':
                    self.updated_at = datetime.fromisoformat(j)
                if i == '__class__':
                    continue
                if i == 'id':
                    self.id = j
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            

    def __str__(self):
         """
        The function returns a string representation of the object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        pass

    def to_dict(self):
        pass
