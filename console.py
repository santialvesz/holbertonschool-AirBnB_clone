#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

def do_quit(self, line):
    """Method to exit the HBNB console"""
    exit()

def do_EOF(self, line):
    """"""
    exit()

def emptyline(self):
    pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()