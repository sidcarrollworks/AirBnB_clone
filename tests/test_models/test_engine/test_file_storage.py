#!/usr/bin/python3
'''
    testing for file storage
'''
import unittest
import json
import sys
import io
import os
import uuid
import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    '''class for testing file storage'''
    def test_create_inst(self):
        '''create instance of filestorage'''
        inst = FileStorage()
        self.assertIsInstance(inst, FileStorage)

    def test_all(self):
        '''test all'''
        inst = FileStorage()
        alll = FileStorage.all()
        self.assertIsInstance(alll, dict)

    def test_save(self):
        '''test save'''
        inst = FileStorage()
        inst.save()
        try:
            os.path.exists('file.json')
        except FileNotFoundError as error:
            print(error)

    def test_new(self):
        ''' test new'''
        inst = FileStorage()
        base = BaseModel()
        inst.new(base)
        alll = inst.all()
        test = inst.__class__.__name__ + '.' + base.id
        self.assertIn(test_entry, test_dict)
