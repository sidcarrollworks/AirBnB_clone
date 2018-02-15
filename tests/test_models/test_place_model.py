#!/usr/bin/python3
"""
Contains tests for class Place
"""


from datetime import datetime
import inspect
from models import base_model
from models.place import Place
import pep8
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
        self.assertTrue("name" in my_place.__dir__())
