#!/usr/bin/python3
"""
Console module for the AirBnB clone project.
Contains the entry point of the command interpreter.
"""

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
