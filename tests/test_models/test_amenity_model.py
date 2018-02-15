#!/usr/bin/python3
"""
Contains tests for class amenity
"""


from datetime import datetime
import inspect
from models import base_model
from models.amenity import Amenity
import pep8
import unittest
import string
from io import StringIO
import sys

BaseModel = base_model.BaseModel


class TestAmenityClass(unittest.TestCase):
    '''Tests for Amenity'''

    def test_props(self):
        '''Test the properties of amenity'''
        my_am = Amenity()
        self.assertTrue("name" in my_am.__dir__())
