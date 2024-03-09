#!/usr/bin/python3
"""
Command interpreter module for the AirBnB clone project.
"""

import cmd
from models import storage


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
        EOF command to exit the program.
        """
        return True

    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it, and prints the id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        if arg not in storage.classes():
            print("** class doesn't exist **")
            return

        new_instance = storage.classes()[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance.
        Usage: show <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances.
        Usage: all or all <class name>
        """
        objs = storage.all()

        if arg and arg not in storage.classes():
            print("** class doesn't exist **")
            return

        if arg:
            objs = {k: v for k, v in objs.items() if arg == k.split('.')[0]}

        print([str(v) for v in objs.values()])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = storage.all()[key]
        setattr(obj, args[2], args[3].strip('"'))
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

