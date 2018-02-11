#!/usr/bin/python3
'''
    Hbnb console
'''

import cmd
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
    """comand processor"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        '''quits console'''
        return True

    def do_quit(self, line):
        '''quits console'''
        return  True

    def do_create(self, *args):
        '''Usage: create [class]'''
        if not args[0]:
            print('** class name missing **')
            return
        try:
            inst = eval(args[0])()
            models.storage.save()
            print(inst.id)
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
        '''prints all instances'''
        stored = models.storage.all()
        new_list = ['[']
        flag = 1

        if not args[0]:
            for val in stored.values():
                if flag:
                    new_list.append(str(val))
                    flag = 0
                else:
                    new_list.append(', ')
                    new_list.append(str(val))
        else:
            try:
                class_name = eval(args[0])
            except NameError:
                print ("** class doesn't exist **")
                return
            for val in stored.values():
                if val.__class__.__name__ == args[0]:
                    if flag:
                        new_list.append(str(val))
                        flag = 0
                    else:
                        new_list.append(', ')
                        new_list.append(str(val))
        new_list.append(']')
        print("".join(new_list))

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
            return
        stored = models.storage.all()
        for obj in stored.values():
            if class_id == obj.id:
                try:
                    attr_n = sep_args[2]
                    try:
                        attr_v = sep_args[3]
                        setattr(obj, attr_n, attr_v[1:-1])
                        models.storage.save()
                        return
                    except IndexError:
                        print('** value missing **')
                        return
                except IndexError:
                    print('** attribute name missing **')
                    return
        print('** no instance **')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
