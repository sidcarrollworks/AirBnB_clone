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
        self.assertIsInstance(my_user(), BaseModel)
