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

    # Test for square id
    def test_id(self):
        """Testing square id"""
        sq = Square(3, 0, 0, 5)
        self.assertEqual(5, sq.id)

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
        # Test both *args and **kwargs
        self.square.update(3, 4, **{'x': 3, 'y': 4})
        self.assertEqual("[Square] (3) 0/0 - 4", self.square.__str__())

    # Test dictionary
    def test_to_dictionary(self):
        """Tests to dictionary"""
        sq = Square(1, 2, 3, 5)
        dict_ob = sq.to_dictionary()
        sq1 = Square.create(**dict_ob)
        self.assertNotEqual(sq1, sq)

    def test_dictionary_is(self):
        """Test if objects are similar"""
        sq = Square(1, 3, 4, 5)
        dict_ob = sq.to_dictionary()
        sq1 = Square.create(**dict_ob)
        self.assertIsNot(sq1, sq)

    # Test saving files
    def test_save_none(self):
        """None file name given"""
        import json
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            file_cont = json.load(f)
            self.assertEqual(file_cont, [])

    def test_save_empty(self):
        """Test for Empty file"""
        import json
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            file_cont = json.load(f)
            self.assertEqual(file_cont, [])

    def test_save_input(self):
        """Proper input for file"""
        import json
        sq = Square(1, 2, 3, 4)
        Square.save_to_file([sq])
        with open("Square.json", "r") as f:
            obj_cont = f.read()
            self.assertEqual(json.loads(obj_cont), [{'id': 4,
                                                    'size': 1,
                                                     'x': 2,
                                                     'y': 3}])

    def test_save_zeroargs(self):
        """No arguments given"""
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_load_from_file(self):
        """Testing load from file"""
        Square.save_to_file([self.square])
        list_out = Square.load_from_file()
        self.assertEqual(self.square.width, list_out[0].size)
