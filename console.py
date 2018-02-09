#!/usr/bin/python3
'''
    Hbnb console
'''

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """comand processor"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        '''return end of file signal'''
        return True

    def do_quit(self, line):
        '''quits comsole'''
        return  True

    def do_create(self, *args):
        '''Usage: create [classname]'''
        if not args[0]:
           print('"" class name missing""')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
