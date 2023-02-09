#!/usr/bin/env python3
"""This is the entry point of the interprerter"""


import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """Creates the command interpreter class"""
    prompt = "(hbnb) "

    # Basic instance methods
    def emptyline(self):
        """Handles emptyline + ENTER from the interpreter"""
        pass
    
    # Instance do_*() methods
    def do_quit(self, line):
        """`quit` | `EOF`: command exits the program."""
        return True

    def do_EOF(self, line):
        """`EOF` | `quit`: command exits the program."""
        return True

    def do_create(self, line):
        """
        create <class>: creates a new instance of <class>, and saves the
        new <class> instance into a JSON file, then prints/return the
        instace id of new <class> instance.

        valid <classes>: ['BaseModel']
        """
        command = line.split()
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] !="BaseModel" or len(command) > 1:
            print("** class doesn't exist **")
        else:
            line = BaseModel()
            line.save()
            print(line.id)

    def do_show(self, line):
        """
        show <class> <instance id>: Prints the string representation
        of the instance with matching `instance id`.
        
        valid <classes>: ['BaseModel']
        """
        argv = line.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif len(argv) >= 1 and argv[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            # print the string representation of the object
            storage.reload()
            objs = storage.all()
            key = "{}.{}".format(argv[0], argv[1])
            try:
                obj = objs[key]
                obj = BaseModel(**obj)
                print(obj)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        destroy <class> <instance id>: Destroy the object instance
        of with the matching `instance id`.
        
        valid <classes>: ['BaseModel']
        """
        argv = line.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif len(argv) >= 1 and argv[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            #
            # Destroy macthing instance following these stages:
            #
            # + Create a duplicate copy of all existing objects in JSON file.
            # + Delete the instance of storage (This simply wipe the private
            #   dictionary ``__objects`` that has been preloaded into memory.
            # + Delete matching instance in the duplicate copy.
            # + Serialize the duplicate copy of storage to a fresh new
            #   instance of storage USING ITS ``storage.new()`` method.
            #
            storage = FileStorage()
            storage.reload()
            objs = storage.all()
            key = "{}.{}".format(argv[0], argv[1])
            try:
                del objs[key]
                storage = FileStorage()
                for key, value in objs.items():
                    storage.new(BaseModel(**value))
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """
        all <class>: Prints a list containing string representation
        of all instances in the storage path.
        
        valid <classes>: ['BaseModel']
        """
        argv = line.split()
        if len(argv) >= 1 and argv[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            # Print a list containing all string representation...
            return_list = []
            storage.reload()
            objs = storage.all()
            for key, value in objs.items():
                tmp = BaseModel(**value)
                return_list.append(tmp.__str__())
            print(return_list)

    def do_update(self, line):
        """
        update <class> <instance id> <attribute name> <attribute value>:
        Updates matching instance with a new or existing attribute.

        valid <classes>: ['BaseModel']
        """
        argv = line.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif len(argv) >= 1 and argv[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        elif len(argv) == 2:
            print("** attribute name missing **")
        elif len(argv) == 3:
            print("** value missing **")
        else:
            # Update macthing instance while assuming:
            # + arguments are always in the right order
            # + Each arguments are separated by a space
            # + String argument with a space must be between quotes
            #
            try:
                storage = FileStorage()
                storage.reload()
                objs = storage.all()
                key = "{}.{}".format(argv[0], argv[1])
                obj = objs[key]
                obj = BaseModel(**obj)
                obj.__dict__[argv[2]] = argv[3]
                obj.save()
                objs[key] = obj.to_dict()
                storage = FileStorage()
                for key, value in objs.items():
                    storage.new(BaseModel(**value))
                storage.save()
            except KeyError:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
