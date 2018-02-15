#!/usr/bin/python3
"""
Contains class TestBaseModelDocs and class TestBaseModel
"""


from datetime import datetime
import inspect
from models import base_model
import pep8
import unittest
import string
from io import StringIO
import sys

BaseModel = base_model.BaseModel


class TestBaseModelDocs(unittest.TestCase):
    '''Tests for BaseModel'''
    def test_id(self):
        '''test id'''
        model = BaseModel()
        self.assertEqual(str, type(model.id))

    def test_id_unique(self):
        '''test ids unique'''
        model_1 = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model_1.id, model_2.id)

    def test_id_type(self):
        '''test type of id'''
        model_3 = BaseModel()
        self.assertEqual("<class 'str'>", str(type(model_3.id)))

    def test_id_valid(self):
        '''test if id is correct UUID'''
        model_4 = BaseModel()
        self.assertIs(len(model_4.id), 36)
        self.assertIs(model_4.id[8], "-")
        self.assertIs(model_4.id[13], "-")
        self.assertIs(model_4.id[18], "-")
        self.assertIs(model_4.id[23], "-")
