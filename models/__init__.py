#!/usr/bin/python3
'''
    Unique instance of filestorage
'''
from models.engine.file_storage import FileStorage
from .base_model import BaseModel
from .user import User
from .state import State
from .city import City
from .place import Place
from .amenity import Amenity
from .review import Review

class_dict = {'BaseModel': BaseModel, 'User': User, 'Review': Review,
              'State': State, 'City': City, 'Place': Place, 'Amenity': Amenity}


storage = FileStorage()
storage.reload()
