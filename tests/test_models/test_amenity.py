#!/usr/bin/python3
"""
Contains tests for class amenity
"""
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestAmenityClass(unittest.TestCase):
    '''Tests for Amenity'''

    def test_type(self):
        '''test attr type'''
        my_am = Amenity()
        self.assertTrue(type(my_am.name) is str)

    def test_props(self):
        '''Test the properties of amenity'''
        my_am = Amenity()
        self.assertIsInstance(my_am, BaseModel)
        self.assertTrue(hasattr(my_am, "updated_at"))
        self.assertTrue(hasattr(my_am, "created_at"))
        self.assertTrue(hasattr(my_am, "id"))

    def test_str(self):
        ''' test correct output'''
        my_am = Amenity()
        my_str = "[Amenity] ({}) {}".format(my_am.id, my_am.__dict__)
        self.assertEqual(my_str, str(my_am))

    def test_values(self):
        ''' test correct values'''
        my_am = Amenity()
        fmt = "%Y-%m-%dT%H:%M:%S.%f"
        my_dict = my_am.to_dict()
        self.assertEqual(my_dict['__class__'], 'Amenity')
        self.assertEqual(type(my_dict['created_at']), str)
        self.assertEqual(type(my_dict['updated_at']), str)
        self.assertEqual(my_dict['created_at'], my_am.created_at.strftime(fmt))
        self.assertEqual(my_dict['updated_at'], my_am.updated_at.strftime(fmt))
