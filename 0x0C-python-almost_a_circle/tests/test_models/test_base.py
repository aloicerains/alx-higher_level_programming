#!/usr/bin/python3
"""Test cases for the base.py"""

import unittest
from models.square import Square
from models.base import Base
import json


class TestBaseClass(unittest.TestCase):
    """The class tests cases for base class."""

    def test_no_id(self):
        """No id is provided for base class"""
        t = Base()
        self.assertEqual(1, t.id)

    def test_id(self):
        """An instance is given an Id."""
        t = Base(34)
        self.assertEqual(34, t.id)

    def test_negative_id(self):
        """An instance with negative id"""
        t = Base(-45)
        self.assertEqual(-45, t.id)

    def test_string_id(self):
        """An instance of string id argument"""
        t = Base("Ozark")
        self.assertEqual("Ozark", t.id)

    def test_dict_id(self):
        """Instance of dictionary Id argument"""
        t = Base({'x': 3, 'u': 8})
        self.assertEqual({'x': 3, 'u': 8}, t.id)

    # Tests on test_to_json
    def test_to_json_value(self):
        """Test string values"""
        sq = Square(1, 0, 0, 9)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string), [{"id": 9, "y": 0,
                                                    "size": 1, "x": 0}])

    def test_to_json_None(self):
        """Test None argument"""
        json_st = Base.to_json_string(None)
        self.assertEqual(json_st, "[]")

    def test_to_json_empty(self):
        """test to_json Empty"""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_from_json_string(self):
        """test from json_string"""
        sq = Square(1, 0, 0, 234)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        json_list = Base.from_json_string(json_string)
        self.assertEqual(json_list, [{'size': 1, 'x': 0, 'y': 0, 'id': 234}])

    def test_from_json_none(self):
        """Test from json none"""
        json_list = Base.from_json_string(None)
        self.assertEqual(json_list, [])

    def test_from_json_empty(self):
        """test from json none"""
        json_list = Base.from_json_string([])
        self.assertEqual(json_list, [])

