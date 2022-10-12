#!/usr/bin/python3
"""Console"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command Interpreter"""
    prompt = '(hbnb)'

    def do_quit(self, args):
        """Method to exit the HBNB console"""
        exit()

    def do_EOF(self, line):
        """"""
        exit()

    def emptyline(self):
        pass

    def help(self):
        print("Quit command to exit the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()