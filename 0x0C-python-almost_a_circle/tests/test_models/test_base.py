#!/usr/bin/python3
"""
UNITTESSTS FOR BASE MODULE
Run this code from the roo of the repo with either:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_base.py
"""
import os
import json
import pep8
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestPycodestyle(unittest.TestCase):
    """class to confirm all the code is pep8 compliant
    pep8 models/base.py
    pep8 test/test_models/test_base.py

    Args:
        unittest (testcase): pep8 code
    """

    def test_pycodestyle(self):
        """pycodestyle(pep8 renamed)
        """
        linter = pep8.StyleGuide(quiet=False)
        err_count = 0
        data = ["models/base.py", "tests/test_models/test_base.py"]
        err_count += linter.check_files(data).total_errors
        self.assertEqual(err_count, 0, 'Warning: pycodestyle Error')


class TestBase(unittest.TestCase):
    """test Base Module

    Args:
        unittest (TestCase): single test cases
    """

    def setUp(self):
        """setup test object
        """
        pass

    def tearDown(self):
        """cleanup test data
        """
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass

    """TEST CASE: CLASS ATTRIBUTES"""

    def test_alloc_id(self):
        """Test id allocation"""
        self.assertTrue(Base(700), self.id == 700)
        self.assertTrue(Base(42), self.id == 42)
        self.assertTrue(Base(-80), self.id == -80)
        self.assertTrue(Base(1), self.id == 1)

    def test_default_id(self):
        """Test default id allocation and increment"""
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)
        self.assertTrue(Base(), self.id == 3)

    def test_acCess_private_attr(self):
        """Attribute Error
        Private Attribute not directly accessible"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
            print(Base.nb_objects)

    """TEST CASE: ARGS COUNT"""

    def test_too_many_args(self):
        """TypeError: Too many args"""
        with self.assertRaises(TypeError):
            Base(1, 1)

    """TEST CASE: CLASS NAME"""

    def test_class_name(self):
        """Test case: class name == Base"""
        self.assertTrue(Base(42), self.__class__ == Base)

    """TEST CASE: Dictionary to JSON string"""

    def test_to_json_string(self):
        """Test that returns the JSON string"""
        obj_in_1 = {"id": 42, "width": 6, "height": 9, "x": 4, "y": 2}
        obj_in_2 = {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}
        obj_to_json_str = Base.to_json_string([obj_in_1, obj_in_2])
        self.assertTrue(type(obj_in_1) == dict)
        self.assertTrue(type(obj_to_json_str) == str)
        self.assertTrue(obj_to_json_str,
                        [{"id": 42, "width": 6, "height": 9, "x": 4, "y": 2},
                         {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}])

    def test_none_to_json_string(self):
        """Test If list_dictionaries is None, return the string: []"""
        none_data = None
        none_str = Base.to_json_string([none_data])
        self.assertTrue(type(none_str) == str)
        self.assertTrue(none_str, "[]")

    def test_empty_to_json_string(self):
        """If list_dictionaries is empty, return the string: "[]"""
        emtee = dict()
        emtee_str = Base.to_json_string([emtee])
        self.assertTrue(len(emtee) == 0)
        self.assertTrue(type(emtee_str) == str)
        self.assertTrue(emtee_str, "[]")

    # TEST CASE: JSON string to dictionary
    def test_from_json_string(self):
        """Test: returns the list of the JSON string
            representation json_string"""
        src_str = '[{"id": 2, "width": 2, "height": 7, "x": 2, "y": 52},\
               {"id": 7, "width": 27, "height": 28, "x": 1, "y": 1}]'
        str_rep = Base.from_json_string(src_str)
        self.assertTrue(type(str_rep) == list)
        self.assertTrue(type(src_str) == str)
        self.assertTrue(type(str_rep[0]) == dict)
        self.assertTrue(str_rep,
                        [{"id": 2, "width": 2, "height": 7, "x": 2, "y": 52},
                         {"id": 7, "width": 27, "height": 28, "x": 1, "y": 1}])
        self.assertTrue(str_rep[0],
                        {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5})

    def test_from_json_string_none(self):
        """Test case: If json_string is None, return an empty list"""
        none_type = None
        none_rep = Base.from_json_string(none_type)
        self.assertTrue(type(none_rep) == list)
        self.assertTrue(none_rep == [])

    def test_from_json_string_empty(self):
        """Test case: If json_string is None or empty, return an empty list"""
        empty_json = ""
        empty_rep = Base.from_json_string(empty_json)
        self.assertTrue(type(empty_rep) == list)
        self.assertTrue(empty_rep == [])

    """TEST CASES: Dictionary to Instance"""

    def test_create_module(self):
        """Test: returns an instance with all attributes already set"""
        r_str = Rectangle(3, 500, 50, 50, 1)
        created = r_str.to_dictionary()
        instance = Rectangle.create(**created)
        self.assertEqual(str(r_str), '[Rectangle] (1) 50/50 - 3/500')
        self.assertEqual(str(instance), '[Rectangle] (1) 50/50 - 3/500')
        self.assertIsNot(r_str, instance)

    """TEST CASE: File to instances """

    def test_save_to_file(self):
        """Test case: save_to_file that writes the JSON string
        representation of list_objs to a file"""
        rex = Rectangle(5, 4, 3, 2, 1)
        rex2 = Rectangle(2, 4, 6, 8, 10)
        Rectangle.save_to_file([rex, rex2])
        with open("Rectangle.json", "r") as json_:
            self.assertEqual(
                json.dumps([rex.to_dictionary(), rex2.to_dictionary()]),
                json_.read())

    def test_save_none_to_file(self):
        """Test case: If list_objs is None, save an empty list"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as none_file:
            self.assertEqual('[]', none_file.read())

    def test_empty_none_to_file(self):
        """Test case: If list_objs is empty, save an empty list"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as empty_file:
            self.assertEqual('[]', empty_file.read())

    """TEEST CASES: File to instances"""

    def test_load_from_file(self):
        """Test that load_from_file(cls): returns a list of instances"""
        r = Rectangle(10, 7, 2, 8, 42)
        r2 = Rectangle(2, 4, 2, 2, 69)
        Rectangle.save_to_file([r, r2])
        strep = Rectangle.load_from_file()
        self.assertEqual(len(strep), 2)
        for key, value in enumerate(strep):
            if key == 0:
                self.assertEqual(str(value), '[Rectangle] (42) 2/8 - 10/7')
            if key == 1:
                self.assertEqual(str(value), '[Rectangle] (69) 2/2 - 2/4')

    def test_load_from_none_file(self):
        """Test:If the file doesn’t exist, return an empty list"""
        Rectangle.save_to_file(None)
        NO_FILE = Rectangle.load_from_file()
        self.assertEqual(type(NO_FILE), list)
        self.assertEqual(len(NO_FILE), 0)
