import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

def do_quit(self, line):
    """Method to exit the HBNB console"""
    exit()

def help_quit():
    """"""
    print()

def do_EOF(self, line):
    """"""
    return True

def emptyline(self):
    pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()