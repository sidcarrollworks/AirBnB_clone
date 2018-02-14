#!/usr/bin/python3
'''
    Hbnb console
'''

import cmd
from models.base_model import BaseModel
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """comand processor"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        '''quits console'''
        return True

    def do_quit(self, line):
        '''quits console'''
        return True

    def emptyline(self):
        pass

    def do_create(self, *args):
        '''Usage: create [class]'''
        if not args[0]:
            print('** class name missing **')
            return
        try:
            inst = eval(args[0])()
            print(inst.id)
            models.storage.save()
        except NameError:
            print("** class doesn't exist **")
            return

    def do_show(self, *args):
        '''Usage: show [class] [id]'''
        if not args[0]:
            print('** class name missing **')
            return
        try:
            sep_args = args[0].split()
            class_name = sep_args[0]
            test = eval(class_name)
            class_id = sep_args[1]
        except NameError:
            print("** class doesn't exist **")
            return
        except IndexError:
            print('** instance id missing **')
            return
        stored = models.storage.all()
        for i in stored.values():
            if class_name == i.__class__.__name__ and class_id == i.id:
                print(i)
                return
        print('** no instance found **')

    def do_destroy(self, *args):
        '''Usage: destroy [class] [id]'''
        if not args[0]:
            print('** class name missing **')
            return
        try:
            sep_args = args[0].split()
            class_name = sep_args[0]
            test = eval(class_name)
            class_id = sep_args[1]
        except NameError:
            print("** class doesn't exist **")
            return
        except IndexError:
            print ('** instance id missing **')
            return
        stored = models.storage.all()
        for key, val in stored.items():
            if class_name == val.__class__.__name__ and class_id == val.id:
                del stored[key]
                models.storage.save()
                return
        print('** no instance found **')

    def do_all(self, *args):
        temp_dict = models.storage.all()
        obj_list = []
        if not args[0]:
            for key, val in temp_dict.items():
                obj_list.append(val)
            print(obj_list)
        else:
            try:
                test = eval(args[0])
                for key, val in temp_dict.items():
                    if sep_arg[0] in key:
                        obj_list.append(val)
                print(obj_list)
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, *args):
        '''update <class name> <id> <attribute name> "<attribute value>"'''
        if not (args[0]):
            print('** class name missing **')
            return
        try:
            sep_args = args[0].split()
            class_name = sep_args[0]
            test = eval(class_name)
            class_id = sep_args[1]
        except NameError:
            print("** class doesn't exist **")
            return
        except IndexError:
            print('** instance id missing **')
        stored = models.storage.all()
        for obj in stored.values():
            if class_id == obj.id:
                try:
                    attr_n = sep_args[2]
                    try:
                        attr_v = sep_args[3]
                        setattr(obj, attr_n, attr_v[1:-1])
                        obj.save()
                        print('this has been saved')
                        return
                    except IndexError:
                        print('** value missing **')
                        return
                except IndexError:
                    print('** attribute name missing **')
                    return
        print('** no instance found **')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
