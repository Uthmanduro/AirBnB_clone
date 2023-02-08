#!/usr/bin/env python3
"""this is the entry point of the interprerter"""


import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """creates the command interpreter class"""
    prompt = "(hbnb) "
    def emptyline(self):
        """wont execute when an empty libe is run"""
        pass
    def do_quit(self, line):
        """used to exit the program"""
        return True

    def do_EOF(self, line):
        """pass EOF as string to cdm"""
        return True

    def do_create(self, line):
        """creates a new instance of BaseModel and prints the ID"""
        command = line.split()
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] !="BaseModel" or len(command) > 1:
            print("** class doesn't exist **")
        else:
            line = BaseModel()
            line.save()
            print(line.id)

    def do_show(self, ):
        """prints the string representation of an instance"""
        print(BaseModel.id.__str__())

if __name__ == '__main__':
    HBNBCommand().cmdloop()
