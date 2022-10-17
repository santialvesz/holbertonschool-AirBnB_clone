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

    def do_create(self, line):
        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if args[0] not in HBNBCommand._classes:
            print("** class doesn't exist **")
            return

        new_obj = globals()[args[0]]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, line):
        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if args[0] not in HBNBCommand._classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        k = args[0] + "." + args[1]
        instance = FileStorage()
        new = models.storage.all()

        for key, value in new.items():
            if key == k:
                print(value)
                return
        print("** no instance found **")




if __name__ == '__main__':
    HBNBCommand().cmdloop()
