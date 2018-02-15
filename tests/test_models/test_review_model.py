#!/usr/bin/python3
"""
Contains class TestBaseModelDocs and class TestBaseModel
"""


from datetime import datetime
import inspect
from models import base_model
from models.review import Review
import unittest
import string
from io import StringIO
import sys

BaseModel = base_model.BaseModel


class TestReviewClass(unittest.TestCase):
    '''Tests for Review'''

    def test_props(self):
        my_rev = Review()
        self.assertTrue("user_id" in my_rev.__dir__())
