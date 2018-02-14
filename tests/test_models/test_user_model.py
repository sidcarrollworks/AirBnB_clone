#!/usr/bin/python3
"""
Contains tests for class User
"""


from datetime import datetime
import inspect
from models import base_model
from models.user import User
import pep8
import unittest
import string
from io import StringIO
import sys

BaseModel = base_model.BaseModel


class TestPlaceClass(unittest.TestCase):
    '''Tests for User'''

    def test_props(self):
        '''Test the properties of user'''
        my_user = User()
        self.assertTrue("first_name" in my_user.__dir__())
