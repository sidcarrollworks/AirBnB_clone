#!/usr/bin/python3
'''Test console'''


import sys
import unittest
import console
from io import StringIO
HBNBCommand = console.HBNBCommand


class TestConsole(unittest.TestCase):
    '''Class console'''
    def test_docstring(self):
        '''test for docstring'''
        self.assertTrue(len(console.__doc__) > 0, "Needs a docstring")
