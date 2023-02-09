#!/usr/bin/env python3
"""This is the entry point of the interprerter"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """Creates the command interpreter class"""
    prompt = "(hbnb) "
    valid_classes = ['BaseModel', 'User']

    # Basic instance methods
    def emptyline(self):
        """Handles emptyline + ENTER from the interpreter"""
        pass
    
    # Instance do_*() methods
    def do_quit(self, line):
        """
        `quit` | `EOF`: command exits the program.
        """
        return True

    def do_EOF(self, line):
        """
        `EOF` | `quit`: command exits the program.
        """
        return True

    def do_create(self, line):
        """
        create <class>: creates a new instance of <class>, and saves the
        new <class> instance into a JSON file, then prints/return the
        instace id of new <class> instance.

        valid <classes>: ['BaseModel', 'User']
        """
        argv = line.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif len(argv) >= 1 and argv[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            obj = eval("{}()".format(argv[0]))
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """
        show <class> <instance id>: Prints the string representation
        of the instance with matching `instance id`.
        
        valid <classes>: ['BaseModel', 'User']
        """
        argv = line.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif len(argv) >= 1 and argv[0] not in self.valid_classes:
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
                print(obj)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        destroy <class> <instance id>: Destroy the object instance
        of with the matching `instance id`.
        
        valid <classes>: ['BaseModel', 'User']
        """
        argv = line.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif len(argv) >= 1 and argv[0] not in self.valid_classes:
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
                if len(objs) != 1:
                    del objs[key]
                    storage = FileStorage()
                    for key, obj in objs.items():
                        storage.new(obj)
                else:
                    del objs[key]
                    objs = {}
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """
        all [class]: Prints a list containing string representation
        of all instances in the storage path, optional `[class]` name
        can be passed to print only a list of  matching object with
        the class.
        
        valid <classes>: ['BaseModel', 'User']
        """
        argv = line.split()
        if len(argv) >= 1 and argv[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(argv) >= 1 and argv[0] in self.valid_classes:
            # Print a list containing only specified class objects
            return_list = []
            storage.reload()
            objs = storage.all()
            for key, obj in objs.items():
                if key == ("" + argv[0] + "." + obj.__dict__["id"]):
                    return_list.append(obj.__str__())
            print(return_list)
        else:
            # Print a list containing all class objects in storage
            return_list = []
            storage.reload()
            objs = storage.all()
            for key, obj in objs.items():
                return_list.append(obj.__str__())
            print(return_list)

    def do_update(self, line):
        """
        update <class> <instance id> <attribute name> <attribute value>:
        Updates matching instance with a new or existing attribute.

        valid <classes>: ['BaseModel', 'User']
        """
        argv = line.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif len(argv) >= 1 and argv[0] not in self.valid_classes:
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
                storage.reload()
                objs = storage.all()
                key = "{}.{}".format(argv[0], argv[1])
                obj = objs[key]
                try:
                    Type = type(obj.__dict__[argv[2]])
                    obj.__dict__[argv[2]] = Type(argv[3])
                except KeyError:
                    obj.__dict__[argv[2]] = argv[3]
                obj.save()
            except KeyError:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
