#!/usr/bin/python3
"""is the console of the project"""


import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Define a console Class"""

    prompt = "(hbnb) "
    _classes = ["BaseModel", "User", "State", "City",
                "Amenity", "Place", "Review"]

    def do_quit(self, args):
        """funtion quit"""
        exit()

    def do_EOF(self, l):
        """function EOF"""
        print("")
        exit()

    def emptyline(self):
        """Function emptyline"""
        pass

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

def do_show(self, args):
        """Prints the string representation of
        an instance based on the class name and id"""
        my_args = args.split()
        if len(my_args) == 0:
            print("** class name missing **")
            return
        my_dict = storage.all()
        for key, value in my_dict.items():
            if my_args[0] == value.__class__.__name__:
                if len(my_args) == 1:
                    print("** instance id missing **")
                    return
                if my_args[1] == value.id:
                    print(value)
                    return
        for k in dictionary.keys():
            if my_args[0] == k:
                print("** no instance found **")
                return
        print("** class doesn't exist **")

        





if __name__ == '__main__':
    HBNBCommand().cmdloop()
