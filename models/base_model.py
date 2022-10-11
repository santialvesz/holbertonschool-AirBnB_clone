import uuid
from datetime import datetime

class BaseModel():
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:



            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at


def __str__(self):
    return ({} {} {}.format([<class name>] (<self.id>) <self.__dict__>))


def save(self):
    pass

def to_dict(self):
    pass
