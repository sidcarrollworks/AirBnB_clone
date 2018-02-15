#!/usr/bin/python3
"""
Contains tests for class amenity
"""


from datetime import datetime
import inspect
from models import base_model
from models.city import City
import unittest
import string
from io import StringIO
import sys

BaseModel = base_model.BaseModel


class TestCityClass(unittest.TestCase):
    '''Tests for City'''

    def test_inst(self):
        '''Test the properties of city'''
        my_city = City()
        self.assertIsInstance(my_city, BaseModel)

    def test_type(self):
        '''tests type of name'''
        my_city = City()
        name = getattr(my_city, "name")
        self.assertIsInstance(name, str)

        name = getattr(my_city, "state_id")
        self.assertIsInstance(name, str)

    def test_update_after_save(self):
        '''tests if updated_at is set to current datetime'''
        my_city = City()
        prev = my_city.updated_at
        my_city.save()
        self.assertNotEqual(prev, my_city.updated_at)

    def test_class(self):
        '''test __class__ key in dict'''
        my_city = City()
        my_dict = my_city.to_dict()
        self.assertIn('__class__', my_dict)

    def test_to_dict_id(self):
        '''checks if type of id val is a string'''
        my_city = City()
        my_dict = my_city.to_dict()
        self.assertEqual(str, type(my_dict['id']))

    def test_updated_at_dict(self):
        '''test if updated_at is in dictionary'''
        my_city = City()
        my_dict = my_city.to_dict()
        self.assertIn('updated_at', my_dict)

    def test_updated_at_str(self):
        '''test if updated_at is string'''
        my_city = City()
        my_dict = my_city.to_dict()
        self.assertEqual(str, type(my_dict['updated_at']))

    def test_created_at_in_dict(self):
        '''test created_at in dictionary'''
        my_city = City()
        my_dict = my_city.to_dict()
        self.assertIn('created_at', my_dict)

    def test_created_at_is_str(self):
        '''test created_at is string'''
        my_city = City()
        my_dict = my_city.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))

    def test_attr(self):
        '''test class attributes'''
        test1 = City()
        test2 = City()
        self.assertTrue(hasattr(test1, "state_id"))
        self.assertTrue(hasattr(test1, "name"))
        self.assertTrue(test1.id != test2.id)

if __name__ == '__main__':
    unittest.main()
