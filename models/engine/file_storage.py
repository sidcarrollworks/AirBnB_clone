#!/usr/bin/python3
'''
    Serialize and deserializes json
'''

import json
from models.base_model import BaseModel


class FileStorage:
    '''
        class to serialize and deserialize
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''returns object dictionary'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets obj to key'''
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''Saves obj to file'''
        my_dict = {}
        for key, val in FileStorage.__objects.items():
            my_dict[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dumps(my_dict, f)

    def reload(self):
        '''deserializes JSON files'''
        try:
            with open(FileStorage.__file_path, 'r') as f:
                tmp_dict = json.load(f)
            for key, val in tmp_dict.items():
                class_name = val['__class__']
                FileStorage.__object[key] = eval(class_name(**val))

        except FileNotFound:
            pass
