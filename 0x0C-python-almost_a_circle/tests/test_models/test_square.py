#!/usr/bin/python3
"""
UNITTESTS FOR SQUARE MODULE
ALL CODE SHOULD BE IN PYCODESTYLE AND WORK AS EXPECTED
THESE TESTS CAN BE RUN FROM THE ROOT DIR WITH:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_square.py
"""
import unittest
import pep8
from models.square import Square
import io
import contextlib


class TestSquare(unittest.TestCase):
    """TESTS FOR THE SQUARE MODULE

    Args:
        unittest (cls): single test cases
    """

    def test_class_style(self):
        """TEST: PEP8 now pycodestyle"""
        style = pep8.StyleGuide(quit=True)
        check_style = style.check_files(['models/square.py'])
        self.assertEqual(
            check_style.total_errors, 0,
            "WARNING: pycodestyle error"
        )
    """TEST CLASS"""

    def test_class_type(self):
        """Test: type class"""
        s = Square(10)
        self.assertEqual(type(s), Square)

    def test_class_str(self):
        """Test: class str"""
        sq_str = Square(666, 9, 8, 7)
        sq_str.size = 42
        self.assertEqual(str(sq_str), '[Square] (7) 9/8 - 42')

    """TEST ATTRIBUTES"""

    def test_attr_setter(self):
        """TEST: set values"""
        sample_sq = Square(1, 2, 3, 401)
        self.assertTrue(sample_sq.width == 1)
        self.assertTrue(sample_sq.height == 1)
        self.assertTrue(sample_sq.size == 1)
        self.assertTrue(sample_sq.x == 2)
        self.assertTrue(sample_sq.y == 3)
        self.assertTrue(sample_sq.id == 401)

    def test_attr_getter(self):
        """TEST: get values"""
        default_sq = Square(3005)
        self.assertTrue(default_sq.height == 3005)
        self.assertTrue(default_sq.size == 3005)
        self.assertTrue(default_sq.x == 0)
        self.assertTrue(default_sq.y == 0)
        self.assertTrue(default_sq.id is not None)

    def test_attr_validation_type(self):
        """TEST: attribute validation for wrong types"""
        err = "width must be an integer"
        with self.assertRaisesRegex(TypeError, err):
            Square("10")
            Square([10, 3])
            Square({20, })
            Square({"d": 20})
            Square(None)
            Square((30, 20), 4)

    def test_attr_negative_values(self):
        """TEST: attribute validation for invalid ints"""
        err_msg = "width must be > 0"
        with self.assertRaisesRegex(ValueError, err_msg):
            Square(-1)
            Square(9).size(-9)

    def test_attr_size_type(self):
        """TEST: size error when wrong obj type"""
        r1 = Square(101)

        with self.assertRaises(TypeError):
            r1.size = "Hi"
            r1.size = 1.5
            r1.size = (2, 8)
            r1.size = [4, 7]
            r1.size = {"hi": 5, "world": 8}
            r1.size = ''
            r1.size = None

    def test_attr_size_zero(self):
        """TEST: size == 0"""
        r1 = Square(6)
        with self.assertRaises(ValueError):
            r1.size = 0

    """TEST METHODS"""

    def test_to_dictionary(self):
        """TEST: to dictionary method"""
        src_str = Square(6, 1, 9, 444).to_dictionary()
        self.assertEqual(type(src_str), dict)
        s2 = Square(10, 10)
        s2.update(**src_str)
        self.assertEqual(str(s2), '[Square] (444) 1/9 - 6')

    def test_display(self):
        """TEST: display method"""
        with io.StringIO() as output_buffer, contextlib.redirect_stdout(output_buffer):
            Square(3).display()
            grid = output_buffer.getvalue()
        self.assertEqual(grid, '###\n###\n###\n')
        with io.StringIO() as output_buffer, contextlib.redirect_stdout(output_buffer):
            Square(3, 1, 2).display()
            s_grid = output_buffer.getvalue()
        self.assertEqual(s_grid, '\n\n ###\n ###\n ###\n')

    def test_update(self):
        """TEST: update method"""
        my_sq = Square(1, 1, 1, 1)
        my_sq.update(8, 8, 8, 8)
        self.assertEqual(str(my_sq), '[Square] (8) 8/8 - 8')
        my_sq.update()
        self.assertEqual(str(my_sq), '[Square] (8) 8/8 - 8')
        my_sq.update(88)
        self.assertEqual(str(my_sq), '[Square] (88) 8/8 - 8')
        my_sq.update(99, 5)
        self.assertEqual(str(my_sq), '[Square] (99) 8/8 - 5')
        my_sq.update(66, 42, 50, 50)
        self.assertEqual(str(my_sq), '[Square] (66) 50/50 - 42')
        """Test method: update(*kwargs)"""
        my_sq.update(id=69, size=42, nokey=99)
        self.assertEqual(str(my_sq), '[Square] (69) 50/50 - 42')

    """TEST ARGS COUNT"""

    def test_too_many_args(self):
        """TEST: excessive args given"""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6, 7)

    def test_too_few_args(self):
        """TEST: inadequate args given"""
        with self.assertRaises(TypeError):
            Square()

    def test_none_args(self):
        """TEST: none as argument"""
        with self.assertRaises(TypeError):
            Square(None)
