#!/usr/bin/python3
"""
Contains tests for class amenity
"""


from datetime import datetime
import inspect
from models import base_model
from models.city import City
import pep8
import unittest
import string
from io import StringIO
import sys

BaseModel = base_model.BaseModel


class TestCityClass(unittest.TestCase):
    '''Tests for City'''

    def test_props(self):
        '''Test the properties of city'''
        my_city = City()
        self.assertTrue("name" in my_city.__dir__())
