#!/usr/bin/env python3
"""
A unit test module for testing ``models/base_model.py`` module.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class Test_BaseModel(unittest.TestCase):
    """
    Test the basic features of the BaseModel class.
    """

    def test_base_model_instance(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)
