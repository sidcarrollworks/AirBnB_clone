#!/usr/bin/python3
'''
    testing for file storage
'''
import unittest
import json
import uuid
import os
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
        alll = inst.all()
        self.assertIsInstance(alll, dict)

    def test_filestorage(self):
        '''test filestorage'''
        inst = FileStorage()
        self.assertEqual(type(inst), type(FileStorage()))

    def test_reload(self):
        '''test reload'''
        store = FileStorage()
        inst = BaseModel()
        inst_id = inst.id
        store.new(inst)
        store.save()
        store.reload()
        inst_dict = store.all()
        self.assertEqual(type(inst_dict), dict)

    def test_save(self):
        '''test save'''
        base = BaseModel()
        inst = FileStorage()
        inst.new(base)
        inst.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_new(self):
        ''' test new'''
        inst = FileStorage()
        base = BaseModel()
        inst.new(base)
        test_str = "{}.{}".format(base.__class__.__name__, base.id)
        test_dict = inst.all()
        self.assertIn(test_str, test_dict)

    def test_new_2(self):
        """Tests if new method adds obj to __objects."""
        a = FileStorage()
        b = BaseModel()
        a.new(b)
        self.assertTrue('BaseModel.' + b.id in a.all())

    def test_save(self):
        ''' test if it save attributes'''
        inst = BaseModel()
        store = FileStorage()
        inst.my_number = 9
        store.new(inst)
        store.save()
        self.assertEqual(inst.my_number, 9)

    def test_file(self):
        '''test if file exists'''
        inst = BaseModel()
        store = FileStorage()
        store.new(inst)
        store.save()
        self.assertTrue(os.path.exists(store._FileStorage__file_path))
