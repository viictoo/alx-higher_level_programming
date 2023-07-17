#!/usr/bin/python3
"""
UNITTESTS FOR RECTANGLE MODULE
ALL CODE IS REQUIRED TO BE WRITTEN IN PEP8 STYLE
THE TEST FILES CAN BE RUN FROM THE ROOT WITH:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_rectangle.py
"""

import pep8
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Tests for models/rectangle.py"""

    """TEST CASE: CLASS"""

    def test_class_type(self):
        """
        Test if Rectangle class inherit from
        Base class
        """
        test_r1 = Rectangle(10, 20, 1, 2, 99)
        self.assertEqual(type(test_r1), Rectangle)

    def test_class_subclass(self):
        """
        Test if Rectangle class inherit from
        Base class
        """
        self.assertTrue(issubclass(Rectangle, Base))

    """TEST CASE: ATTRIBUTES"""

    def test_attr_setter_getter(self):
        """Test: get and set attributes"""
        r1 = Rectangle(10, 20, 1, 2, 99)
        self.assertTrue(r1.width == 10)
        self.assertTrue(r1.height == 20)
        self.assertTrue(r1.x == 1)
        self.assertTrue(r1.y == 2)
        self.assertTrue(r1.id == 99)

    def test_attr_default_values(self):
        """Test: Default values allocated"""
        r2 = Rectangle(3, 4)
        self.assertTrue(r2.width == 3)
        self.assertTrue(r2.height == 4)
        self.assertTrue(r2.x == 0)
        self.assertTrue(r2.y == 0)
        self.assertTrue(r2.id is not None)

    def test_attr_type(self):
        """Test: validate attribute type"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("str", 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"dict": 20}, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float("inf"))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, None, 1, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, (tuple, 20), 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, [1, 2], 1)

    def test_attr_min_values(self):
        """Test: validate attribute values
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, -1, 1, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 1, 1, -1, 1)

    def test_attr_private(self):
        """Test: access private attributes"""
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
        with self.assertRaises(AttributeError):
            print(Rectangle.__height)
        with self.assertRaises(AttributeError):
            print(Rectangle.__x)
        with self.assertRaises(AttributeError):
            print(Rectangle.__y)

    """TEST CASE: ARG COUNT"""

    def test_args_too_many(self):
        """Test: Escessive number of args passed"""
        with self.assertRaises(TypeError):
            Rectangle(9, 8, 7, 6, 5, 4, 3, 2, 1)

    def test_args_too_few(self):
        """Test: Inadequate number of args"""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(None)
        with self.assertRaises(TypeError):
            Rectangle(404)

    """TEST CASE: METHODS"""

    def test_area(self):
        """Test: area"""
        self.assertEqual(Rectangle(2, 2).area(), 4)
        self.assertEqual(Rectangle(3, 3, 1, 2).area(), 9)
        self.assertEqual(Rectangle(1, 2, 3, 4, 15).area(), 2)

    def test_print(self):
        """Test: __str__"""
        s_print = Rectangle(1, 2, 3, 4, 21)
        self.assertEqual(str(s_print), '[Rectangle] (21) 3/4 - 1/2')

    def test_update_with_args(self):
        """Test: update"""
        update_r = Rectangle(1, 2, 3, 4, 5)
        update_r.update(10, 20, 30, 40, 50)
        self.assertEqual(str(update_r), '[Rectangle] (10) 40/50 - 20/30')

    def test_update_with_args_invalid_y(self):
        """Test: update with invalid args"""
        update_r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            update_r.update(99, 1, 2, 3, "how")

    def test_update_with_args_negative_y(self):
        """Test: update with invalid value"""
        update_r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            update_r.update(99, 1, 2, 3, -99)

    def test_update_with_kwargs(self):
        """Test:update using key words (**kwargs)"""
        update_r = Rectangle(1, 2, 3, 4, 5)
        update_r.update(id=1001)
        self.assertEqual(str(update_r), '[Rectangle] (1001) 3/4 - 1/2')

    def test_update_with_kwargs_multiple(self):
        """Test: update all kwargs"""
        update_r = Rectangle(1, 2, 3, 4, 5)
        update_r.update(id=44, x=770, y=880, width=990)
        self.assertEqual(str(update_r), '[Rectangle] (44) 770/880 - 990/2')

    def test_update_with_mixture_args_kwargs(self):
        """Test: update with invalid kwargs"""
        update_r = Rectangle(1, 2, 3, 4, 5)
        update_r.update(nokey=1000, invalid=2000, testing=3000, id=4000)
        self.assertEqual(str(update_r), '[Rectangle] (4000) 3/4 - 1/2')

    def test_to_dictionary(self):
        """Test: to dictionary"""
        r_to_dict = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        self.assertEqual(type(r_to_dict), dict)
        r_to_dict2 = Rectangle(10, 10)
        r_to_dict2.update(**r_to_dict)
        self.assertEqual(str(r_to_dict2), '[Rectangle] (5) 3/4 - 1/2')


class TestPep8(unittest.TestCase):
    """TEST: pycodestyle violations"""

    def test_pep8(self):
        """TEST FILES STYLE"""
        style_guide = pep8.StyleGuide(quiet=False)
        src = ["models/rectangle.py", "tests/test_models/test_rectangle.py"]
        output = style_guide.check_files(src)
        self.assertEqual(output.total_errors, 0,
                         'PEP 8 style violations found.')
