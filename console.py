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
        '''quits console'''
        return True

    def do_quit(self, line):
        '''quits console'''
        return  True:x

if __name__ == '__main__':
    HBNBCommand().cmdloop()
