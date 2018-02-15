#!/usr/bin/python3
'''
    Serialize and deserializes json
'''

import json
import models


class FileStorage:
    '''
        class to serialize and deserialize
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''returns object dictionary'''
        return self.__objects

    def new(self, obj):
        '''sets obj to key'''
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''Saves obj to file'''
        my_dict = {}
        for key, val in self.__objects.items():
            my_dict[key] = val.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        '''deserializes JSON files'''
        try:
            with open(self.__file_path, 'r') as f:
                tmp_dict = json.load(f)
            for key, val in tmp_dict.items():
                class_name = val.get('__class__')
                if class_name in models.class_dict:
                    self.__objects[key] = models.class_dict[class_name](**val)
        except FileNotFoundError:
            pass
