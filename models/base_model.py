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
            format = '%Y-%m-%dT%H:%M:%S.%f'
            for a in kwargs:
                if a = "id":
                    self.id = kwargs[a]
                if a == "created_at":
                    self.created_at = datetime.strptime(kwargs[a], format)
                if a == "updated_at":
                    self.updated_at = datetime.strptime(kwargs[a], format)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)


    def __str__(self):
        """
        The function returns a string representation of the object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """"
        The save function updates the updated_at attribute of the object to the current time and saves
        the object to the JSON file.
        """
        self.updated_at = datetime.now
        models.storage.save()


    def to_dict(self):
         """
        This function takes in an object and returns a dictionary representation of the object
        """
        pass
