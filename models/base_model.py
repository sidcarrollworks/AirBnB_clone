#!/usr/bin/python3
""" Base Model"""

import uuid
from datetime import datetime


class BaseModel:
    """this is the base model"""
    def __init__(self, *args, **kwargs):
        ''' Initialize public instance attributes'''
        if len(kwargs) is 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            fmt = '%Y-%m-%dT%H:%M:%S.%f'
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'], fmt)
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], fmt)



    def __str__(self):
        """return string in format"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id, self.__dict__)

    def save(self):
        """updates public instance with current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns dictionary of keys/values of instance"""
        my_dict = dict(self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
