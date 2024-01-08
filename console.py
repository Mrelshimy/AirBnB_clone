#!/usr/bin/env python3
"""Console Module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Console class"""

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """ Quit console by typing 'quit' """
        return True
    def do_EOF(self, arg):
        """End operation by typing EOF or Ctrl+d"""
        return True
    def emptyline(self):
        """Empty line responce"""
        pass
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
