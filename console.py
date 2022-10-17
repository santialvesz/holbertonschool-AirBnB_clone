#!/usr/bin/python3
"""Console 0.0.1"""


import cmd
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel

dictionary = {"Amenity": Amenity,
              "BaseModel": BaseModel,
              "City": City,
              "Place": Place,
              "Review": Review,
              "State": State,
              "User": User}


class HBNBCommand(cmd.Cmd):
    """HBNB"""
    prompt = "(hbnb)"

    def emptyline(self):
        """Print Anything"""
        pass

    def do_EOF(self, args):
        """End of File"""
        return True

    def do_quit(self, args):
        """Quit"""
        return True

    def do_create(self, arg):
        """Create a new instance"""
        my_args = arg.split()
        if len(my_args) == 0:
            print("** class name missing **")
            return
        try:
            new_ins = eval(my_args[0])()
            new_ins.save()
            print(new_ins.id)
        except Exception:
            print("** class doesn't exist **")
