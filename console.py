#!/usr/bin/python3
'''
    Hbnb console
'''

import cmd
import models
import shlex


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
        '''covers case when line is left empty'''
        pass

    def do_create(self, args):
        '''Usage: create [class]'''
        if not args:
            print('** class name missing **')
        elif args not in models.class_dict:
            print("** class doesn't exist **")
        else:
            inst = models.class_dict[args]()
            print(inst.id)
            models.storage.save()

    def do_show(self, args):
        '''Usage: show [class] [id]'''
        args = shlex.split(args)
        if len(args) == 0:
            print('** class name missing **')
        elif len(args) == 1:
            print('** instance id missing **')
        elif args[0] not in models.class_dict:
            print("** class doesn't exist **")
        else:
            key = "{}.{}".format(args[0], args[1])
            stored = models.storage.all()
            if key in stored:
                print(stored[key])
            else:
                print('** no instance found **')

    def do_destroy(self, args):
        '''Usage: destroy [class] [id]'''
        args = shlex.split(args)
        if len(args) == 0:
            print('** class name missing **')
        elif len(args) == 1:
            print('** instance id missing **')
        elif args[0] not in models.class_dict:
            print("** class doesn't exist **")
        else:
            key = "{}.{}".format(args[0], args[1])
            stored = models.storage.all()
            if key in stored:
                del stored[key]
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, args):
        '''Usage: all [class]'''
        args = shlex.split(args)
        temp_dict = models.storage.all()
        obj_list = []
        if len(args) == 0:
            for key, val in temp_dict.items():
                obj_list.append(val)
            print(obj_list)
        elif args[0] not in models.class_dict:
            print("** class doesn't exist **")
        else:
            for key, val in temp_dict.items():
                if args[0] in key:
                    obj_list.append(val)
            print(obj_list)

    def do_update(self, args):
        '''update <class name> <id> <attribute name> "<attribute value>"'''
        args = shlex.split(args)
        if len(args) == 0:
            print('** class name missing **')
        elif len(args) == 1:
            print('** instance id missing **')
        elif args[0] not in models.class_dict:
            print("** class doesn't exist **")
        else:
            key = "{}.{}".format(args[0], args[1])
            stored = models.storage.all()
            if key not in stored:
                print('** no instance found **')
            elif len(args) == 2:
                print('** attribute name missing **')
            elif len(args) == 3:
                print('** value missing **')
            else:
                val = stored.get(key)
                setattr(val, args[2], args[3])
                models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
