#!/usr/bin/env python3
"""Console Module"""
import cmd
import sys
import inspect
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
import re
import sys


class HBNBCommand(cmd.Cmd):
    """Console class"""

    prompt = "(hbnb) "

    def default(self, line):
        """ default console operation"""
        try:
            ln = line
            command = ["all", "show", "count", "destroy", "update"]
            classes = ["BaseModel", "User", "Amenity",
                       "City", "Place", "Review", "State"]
            ln = ln.strip()
            first_dot = re.search(r"\.", ln)
            clss = ln[:first_dot.span()[0]]
            ln = ln[first_dot.span()[1]:]
            open_paranthes = re.search(r"\(", ln)
            if open_paranthes is None:
                print(f"*** Unknown syntax: {line}")
                return
            cmnd = ln[:open_paranthes.span()[0]]
            ln = ln[open_paranthes.span()[1]:]
            if clss == "" or cmnd not in command:
                print(f"*** Unknown syntax: {line}")
                return
            if clss not in classes:
                print("** class doesn't exist **")
                return
            if ln is None:
                print(f"*** Unknown syntax: {line}")
                return
            close_paranthes = re.search(r"\)", ln)
            if close_paranthes is None:
                print(f"*** Unknown syntax: {line}")
                return
            ln = ln[:close_paranthes.span()[0]]
            if cmnd == "all":
                self.do_all(f"{clss}.")
            elif cmnd == "count":
                self.do_count(clss)
            elif cmnd == "show":
                if len(ln) < 3:
                    print("** instance id missing **")
                self.do_show(f"{clss} {ln[1:-1]}")
            elif cmnd == "destroy":
                if len(ln) < 3:
                    print("** instance id missing **")
                self.do_destroy(f"{clss} {ln[1:-1]}")
            else:
                argmts = ln.strip().split(",", 1)
                argmts[0] = argmts[0].strip()
                if len(argmts[0]) < 3:
                    print("** instance id missing **")
                    return
                else:
                    argmts[0] = argmts[0][1:-1]
                if len(argmts) == 1:
                    self.do_update(f"{clss} {argmts[0]}")
                    return
                argmts[1] = argmts[1].strip()
                if len(argmts) == 2 and argmts[1][0] == "{":
                    dc = re.match(r"\{(.*?)\}", argmts[1])[0]
                    argmts[1] = eval(dc)
                    argmts.insert(0, clss)
                    self.do_update(argmts)
                    return
                ls = argmts[1].split(",")
                argmts.pop(1)
                for ele in ls:
                    ele = ele.strip()
                    argmts.append(ele)
                if len(argmts) == 2:
                    self.do_update(f"{clss} {argmts[0]} {argmts[1]}")
                    return
                if len(argmts) >= 3:
                    argmts[1] = eval(argmts[1])
                    if type(eval(argmts[2])) is not str:
                        argmts[2] = eval(argmts[2])
                    self.do_update(f"{clss} {argmts[0]} \
{argmts[1]} {argmts[2]}")
        except AttributeError:
            print(f"*** Unknown syntax: {line}")

    def do_quit(self, arg):
        """ Quit console by typing 'quit' """
        if not sys.stdin.isatty():
            print()
        return True

    def do_EOF(self, arg):
        """End operation by typing EOF or Ctrl+d"""
        if not sys.stdin.isatty():
            print()
        return True

    def emptyline(self):
        """Empty line responce"""
        if not sys.stdin.isatty():
            print()

    def do_create(self, ModelName):
        """Create a new instance command"""
        if not sys.stdin.isatty():
            print()
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
        if not sys.stdin.isatty():
            print()
        clsmembers = dict(inspect.getmembers(sys.modules[__name__],
                                             inspect.isclass))
        args_list = args.split()
        if len(args_list) < 1:
            print("** class name missing **")
            return
        elif args_list[0] not in clsmembers.keys():
            print("** class doesn't exist **")
            return
        elif len(args_list) < 2:
            print("** instance id missing **")
            return
        else:
            all_objs = storage.all()
            get_obj = f"{args_list[0]}.{args_list[1]}"
            for key, value in all_objs.items():
                if key == get_obj:
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """Destroy command to delete an object based on class and id"""
        if not sys.stdin.isatty():
            print()
        clsmembers = dict(inspect.getmembers(sys.modules[__name__],
                                             inspect.isclass))
        args_list = args.split()
        if len(args_list) < 1:
            print("** class name missing **")
            return
        elif args_list[0] not in clsmembers.keys():
            print("** class doesn't exist **")
            return
        elif len(args_list) < 2:
            print("** instance id missing **")
            return
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
        if not sys.stdin.isatty():
            print()
        clsmembers = dict(inspect.getmembers(sys.modules[__name__],
                                             inspect.isclass))
        all_objs_list = []
        all_objs = storage.all()
        if args:
            if args not in clsmembers.keys() \
               and args[:-1] not in clsmembers.keys():
                print("** class doesn't exist **")
                return
        if '.' in args:
            for model, obj in all_objs.items():
                if args in model:
                    all_objs_list.append(obj.__str__())
            print(all_objs_list)
        else:
            for obj in all_objs.values():
                all_objs_list.append(obj.__str__())
            print(all_objs_list)

    def do_count(self, args):
        """Prints count of instances
        of a class"""
        if not sys.stdin.isatty():
            print()
        clsmembers = dict(inspect.getmembers(sys.modules[__name__],
                                             inspect.isclass))
        all_objs = storage.all()
        count = 0
        if args:
            if args[-1] == ".":
                args = args[:-1]
            if args not in clsmembers.keys():
                print("** class doesn't exist **")
                return
            for obj in all_objs.values():
                if args == obj.__class__.__name__:
                    count += 1
            print(count)
        else:
            print("** class name missing **")

    def do_update(self, args):
        """Update command to update an instance based on
        the class name and id by adding or updating attribute"""
        if not sys.stdin.isatty():
            print()
        if type(args) is list:
            dc = args[2]
            all_objs = storage.all()
            get_obj = f"{args[0]}.{args[1]}"
            for key, value in all_objs.items():
                if key == get_obj:
                    for k, v in dc.items():
                        setattr(value, k, v)
                    storage.save()
                    return
            print("** no instance found **")
            return
        clsmembers = dict(inspect.getmembers(sys.modules[__name__],
                                             inspect.isclass))
        args_list = args.split(" ", maxsplit=3)
        if len(args_list) < 1:
            print("** class name missing **")
            return
        elif args_list[0] not in clsmembers.keys():
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
            return
        elif len(args_list) < 3:
            print("** attribute name missing **")
            return
        elif len(args_list) < 4:
            print("** value missing **")
            return
        else:
            if args_list[3][0][0] == '"':
                attrValue = re.match(r'"(.*?)"', args_list[3])
                attrValue = attrValue.group(1).strip()
            else:
                attrValue = re.match(r'^(\w+(?:\.\w+)?)', args_list[3])
                attrValue = eval(attrValue.group(1))
            all_objs = storage.all()
            get_obj = (f"{args_list[0]}.{args_list[1]}")
            for key, value in all_objs.items():
                if key == get_obj:
                    setattr(value, args_list[2], attrValue)
                    storage.save()
                    return
            print("** no instance found **")

    def do_help(self, line):
        """help command"""
        if not sys.stdin.isatty():
            print()
        cmd.Cmd.do_help(self, line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
