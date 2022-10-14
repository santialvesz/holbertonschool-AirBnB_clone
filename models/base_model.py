#!/usr/bin/python3


import uuid
from datetime import datetime
import models


class BaseModel():
    def __init__(self, *args, **kwargs):
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
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
