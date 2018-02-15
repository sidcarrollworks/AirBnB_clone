#!/usr/bin/python3
"""
Contains class TestBaseModelDocs and class TestBaseModel
"""


from datetime import datetime
import inspect
from models import base_model
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

    def test_created_at(self):
        '''Test created_at created'''
        model_5 = BaseModel()
        self.assertEqual(type(model_5.created_at), datetime)

    def test_updated_at(self):
        '''Test updated_at'''
        model_6 = BaseModel()
        self.assertEqual(datetime, type(model_6.updated_at))

    def test_created_and_updated_at_init(self):
        '''created_at and updated_at should be equal at init'''
        model_7 = BaseModel()
        self.assertEqual(model_7.created_at, model_7.updated_at)

    def test_to_dict_type(self):
        """test to_dict returns dictionary"""
        model_8 = BaseModel()
        self.assertEqual(dict, type(model_8.to_dict()))

    def test_to_dict_class(self):
        '''test class in dict'''
        model_9 = BaseModel()
        self.assertEqual("BaseModel", (model_9.to_dict())["__class__"])

    def test_diff(self):
        '''Test 2 instances are diff ids'''
        model_10 = BaseModel()
        model_11 = BaseModel()
        self.assertNotEqual(model_10.id, model_11.id)

    def test_diff_times(self):
        '''test 2 instance have different times'''
        model_12 = BaseModel()
        model_13 = BaseModel()
        self.assertNotEqual(model_12.updated_at, model_13.updated_at)

    def test_created_at_stays_same(self):
        '''test that created at time stays same'''
        model_14 = BaseModel()
        first_created_time = model_14.created_at
        model_14.save()
        self.assertEqual(first_created_time, model_14.created_at)

    def test_updated_at_not_equal(self):
        '''test that the updated time changes'''
        model_15 = BaseModel()
        first_update = model_15.updated_at
        model_15.save()
        self.assertNotEqual(first_update, model_15.updated_at)

    def test_save(self):
        '''test save function'''
        model_15 = BaseModel()
        model_15.save()
        real = type(model_15.updated_at)
        expect = type(datetime.now())
        self.assertEqual(expect, real)

    def test_to_string(self):
        '''test string function'''
        model_16 = BaseModel()
        my_str = str(model_16)
        my_list = ['id', 'created_at', 'updated_at', 'BaseModel']
        test = 0
        for i in my_list:
            if i in my_str:
                test += 1
        self.assertTrue(test == 4)
