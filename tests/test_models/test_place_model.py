#!/usr/bin/python3
"""
Contains tests for class Place
"""


from datetime import datetime
import inspect
from models import base_model
from models.place import Place
import unittest
import string
from io import StringIO
import sys

BaseModel = base_model.BaseModel


class TestPlaceClass(unittest.TestCase):
    '''Tests for Place'''

    def test_props(self):
        '''Test the properties of place'''
        my_place = Place()
        self.assertTrue(type(my_place.city_id) is str)
        self.assertTrue(type(my_place.user_id) is str)
        self.assertTrue(type(my_place.name) is str)
        self.assertTrue(type(my_place.description) is str)
        self.assertTrue(type(my_place.number_rooms) is int)
        self.assertTrue(type(my_place.number_bathrooms) is int)
        self.assertTrue(type(my_place.max_guest) is int)
        self.assertTrue(type(my_place.price_by_night) is int)
        self.assertTrue(type(my_place.latitude) is float)
        self.assertTrue(type(my_place.longitude) is float)
        self.assertTrue(type(my_place.amenity_ids) is list)
