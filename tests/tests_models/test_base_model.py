#!/usr/bin/python3
"""Test cases for BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def test_save(self):
        """Tests the save method"""
        obj = BaseModel()
        test1 = obj.created_at
        test2 = obj.updated_at
        obj.save()
        self.assertEqual(test1, obj.created_at)
        self.assertNotEqual(test2, obj.updated_at)

    def test_str(self):
        """Tests the __str__ method"""
        obj = BaseModel()
        self.assertEqual(str(obj), f"[{obj.__class__.__name__}] ({obj.id})     {obj.__dict__}")

    def test_to_dict(self):
        """Tests the to_dict method"""
        obj = BaseModel()
        obj_dict = {'id': obj.id, 'created_at': obj.created_at, 'updated_at': obj.updated_at}
        self.assertEqual(obj.__dict__, obj_dict)