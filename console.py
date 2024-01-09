#!/usr/bin/env python3
"""Console Module"""
import cmd
import sys
import inspect
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, ModelName):
        """Create a new instance command"""
        clsmembers = dict(inspect.getmembers(sys.modules[__name__],
                                             inspect.isclass))
        if not ModelName:
            print("** class name missing **")
        elif ModelName not in clsmembers.keys():
            print("** class doesn't exist **")
        else:
            ModelName = globals()[ModelName]
            new_obj = ModelName()
            print(new_obj.id)
            storage.save()

    def do_show(self, args):
        """Print the string representation of object based on the class name"""
        clsmembers = dict(inspect.getmembers(sys.modules[__name__],
                                             inspect.isclass))
        args_list = args.split()
        if len(args_list) < 1:
            print("** class name missing **")
            return
        elif len(args_list) < 2:
            print("** instance id missing **")
            return
        elif args_list[0] not in clsmembers.keys():
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            get_obj = (f"{args_list[0]}.{args_list[1]}")
            for key, value in all_objs.items():
                if key == get_obj:
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """Destroy command to delete an object based on class and id"""
        clsmembers = dict(inspect.getmembers(sys.modules[__name__],
                                             inspect.isclass))
        args_list = args.split()
        if len(args_list) < 1:
            print("** class name missing **")
            return
        elif len(args_list) < 2:
            print("** instance id missing **")
            return
        elif args_list[0] not in clsmembers.keys():
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            try:
                del all_objs[(f"{args_list[0]}.{args_list[1]}")]
                storage.save()
            except Exception:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name"""
        clsmembers = dict(inspect.getmembers(sys.modules[__name__],
                                             inspect.isclass))
        if args:
            if args not in clsmembers.keys():
                print("** class doesn't exist **")
                return
        all_objs = storage.all()
        all_objs_list = []
        for obj in all_objs.values():
            all_objs_list.append(obj.__str__())
        print(all_objs_list)

    def do_update(self, args):
        """Update command to update an instance based on
        the class name and id by adding or updating attribute"""
        clsmembers = dict(inspect.getmembers(sys.modules[__name__],
                                             inspect.isclass))
        args_list = args.split()
        if len(args_list) < 1:
            print("** class name missing **")
            return
        elif len(args_list) < 2:
            print("** instance id missing **")
            return
        elif args_list[0] not in clsmembers.keys():
            print("** class doesn't exist **")
        elif len(args_list) < 3:
            print("** attribute name missing **")
            return
        elif len(args_list) < 4:
            print("** value missing **")
            return
        else:
            all_objs = storage.all()
            get_obj = (f"{args_list[0]}.{args_list[1]}")
            for key, value in all_objs.items():
                if key == get_obj:
                    setattr(value, args_list[2], args_list[3])
                    storage.save()
                    return
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
