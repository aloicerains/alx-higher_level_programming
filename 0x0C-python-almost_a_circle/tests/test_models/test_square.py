#!/usr/bin/python3
"""The module privides tests for the Square class."""

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Provides a series of tests for Square class."""
    def setUp(self):
        """Initialization of method instances"""
        self.square = Square(10)
    
    def tearDown(self):
        """Square destructor"""
        del self.square

    # Tests for square size
    def test_size_int(self):
        """Test integer argument"""
        self.assertEqual(10, self.square.width)
        self.assertEqual(10, self.square.size)

    def test_size_str(self):
        """Testing str argument"""
        with self.assertRaises(TypeError):
            self.square.size = 'str'

    def test_size_nagative(self):
        """Testing negative argument"""
        with self.assertRaises(ValueError):
            self.square.size = -2

    def test_size_zero(self):
        """Testing zero size argument"""
        with self.assertRaises(ValueError):
            self.square.size = 0

    # Tests for square x and y
    def test_xy_int(self):
        """Testing for integer argument"""
        self.square.x = 5
        self.square.y = 8
        self.assertEqual(5, self.square.x)
        self.assertEqual(8, self.square.y)
        sq = Square(3, 3)
        self.assertEqual(0, sq.y)
        self.assertEqual(3, sq.x)

    def test_xy_str(self):
        """Testing string argument"""
        with self.assertRaises(TypeError):
            self.square.x = "str"
        with self.assertRaises(TypeError):
            self.square.y = "st"

    def test_xy_zero(self):
        """Testing zeror argument"""
        self.square.x = 0
        self.square.y = 0
        self.assertEqual(0, self.square.x)
        self.assertEqual(0, self.square.y)

    def test_x_negative(self):
        """Testing negative argument"""
        with self.assertRaises(ValueError):
            self.square.x = -34
        with self.assertRaises(ValueError):
            self.square.y = -45
    
    # Tests for area
    def test_area(self):
        """Tests for the square area"""
        self.assertEqual(100, self.square.area())

    # Test for __str__
    def test_str(self):
        """Testing the return str"""
        sq = Square(10, 4, 5, 8)
        self.assertEqual("[Square] (8) 4/5 - 10", sq.__str__())

    # Test for update
    def test_update(self):
        self.square.update(3, 4)
        self.assertEqual("[Square] (3) 0/0 - 4", self.square.__str__())
