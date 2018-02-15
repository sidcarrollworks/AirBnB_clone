#!/usr/bin/python3
"""
Contains tests for class User
"""


from datetime import datetime
import inspect
from models import base_model
from models.state import State
import unittest
import string
from io import StringIO
import sys

BaseModel = base_model.BaseModel


class TestStateClass(unittest.TestCase):
    '''Tests for User'''

    def test_type(self):
        '''Test the properties of user'''
        my_state = State()
        self.assertTrue(type(my_state.name) is str)
