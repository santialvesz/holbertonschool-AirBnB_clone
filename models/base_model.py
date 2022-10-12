import uuid
from datetime import date, datetime

class BaseModel():
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            format = '%Y-%m-%dT%H:%M:%S.%f'
            for a in kwargs:
                if a == "created_at":
                    self.created_at = datetime.strptime(kwargs, format)
                if a == "updated_at":
                    self.updated_at = datetime.strptime(kwargs, format)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)


    def __str__(self):
        return"[{}] ({}) {}".format(self.__class__.__name__ self.id, self.__dict__)

    def save(self):
        """save doc"""
        self.updated_at = datetime.now
        


    def to_dict(self):
        pass
