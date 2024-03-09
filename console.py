#!/usr/bin/python3
"""
Console module for the AirBnB clone project.
Contains the entry point of the command interpreter.
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exits the program when End of File (EOF) is reached.
        """
        print("")
        return True

    def emptyline(self):
        """
        Override the default behavior of executing the last command
        when an empty line is entered.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it, and prints the id.
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                new_instance = storage.classes()[args[0]]()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance.
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                all_objs = storage.all()
                if key in all_objs:
                    print(all_objs[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                all_objs = storage.all()
                if key in all_objs:
                    del all_objs[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representations of all instances.
        """
        all_objs = storage.all()
        if not arg:
            print([str(all_objs[obj]) for obj in all_objs])
        elif arg in storage.classes():
            print([str(all_objs[obj]) for obj in all_objs if arg in obj])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id.
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                key = args[0] + "." + args[1]
                all_objs = storage.all()
                if key in all_objs:
                    setattr(all_objs[key], args[2], args[3])
                    all_objs[key].save()
                else:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
