#!/usr/bin/python3
"""
Contains tests for class User
"""


from datetime import datetime
import inspect
from models import base_model
from models.user import User
import unittest
import string
from io import StringIO
import sys

BaseModel = base_model.BaseModel


class TestPlaceClass(unittest.TestCase):
    '''Tests for User'''

    def test_isntance(self):
        '''Test the properties of user'''
        my_user = User()
        self.assertIsInstance(my_user, BaseModel)

    def test_attributes(self):
        '''tests user attributes'''
        test1 = User()
        test2 = User()
        self.assertTrue(hasattr(test1, "email"))
        self.assertTrue(hasattr(test1, "password"))
        self.assertTrue(hasattr(test1, "first_name"))
        self.assertTrue(hasattr(test1, "last_name"))
        self.assertTrue(type(test1.email) is str)
        self.assertTrue(type(test1.password) is str)
        self.assertTrue(type(test1.first_name) is str)
        self.assertTrue(type(test1.last_name) is str)
        self.assertTrue(type(test1.id) is str)
        self.assertTrue(test1.id != test2.id)

    def test_save(self):
        ''' test save mdethod'''
        usr = User()
        test_updated = usr.updated_at
        usr.save()
        update = usr.updated_at
        self.assertTrue(test_updated, update)

    def test_str(self):
        '''tests output'''
        usr = User()
        usr_id = usr.id
        usr_dict = usr.__dict__
        st = "[User] ({}) {}".format(usr_id, usr_dict)
        self.assertEqual(st, str(usr))

    def test_created_at(self):
        ''' test created_at'''
        test1 = User()
        test2 = User()
        created1 = test1.created_at
        created2 = test2.created_at
        self.assertIsNot(created1, created2)
        self.assertTrue(type(created1) is datetime)

if __name__ == '__main__':
    unittest.main()
