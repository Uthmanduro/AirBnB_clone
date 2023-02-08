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

    def test_instance_uuid_is_unique(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_instance_created_at_is_str(self):
        base1 = BaseModel()
        self.assertEqual(type(base1.created_at), datetime)

    def test_instance_updated_at_is_str(self):
        base1 = BaseModel()
        self.assertEqual(type(base1.updated_at), datetime)

    def test_save_method(self):
        from time import sleep
        base1 = BaseModel()
        sleep(2)
        base1.save()
        self.assertNotEqual(base1.created_at, base1.updated_at)

    def test_string_representation(self):
        base1 = BaseModel()
        string = "[{}] ({}) {}".format(base1.__class__.__name__,
                                       base1.id, base1.__dict__)
        self.assertEqual(base1.__str__(), string)

    def test_instance_dictionary(self):
        base1 = BaseModel()
        base1.name = "New Instance variable"
        self.assertTrue("__class__" in base1.to_dict())
        self.assertTrue("id" in base1.to_dict())
        self.assertTrue("created_at" in base1.to_dict())
        self.assertTrue("updated_at" in base1.to_dict())
        self.assertTrue("name" in base1.to_dict())
