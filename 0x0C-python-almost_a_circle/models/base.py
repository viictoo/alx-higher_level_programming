#!/usr/bin/python3
"""module for base class"""
import json
import csv
import turtle
import random


class Base():
    """first class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor

        Args:
            id (int, optional): id or nb objects. Defaults to None.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries=[]):
        """serialize json formatted string

        Args:
            list_dictionaries (list, optional): list object. Defaults to [].

        Returns:
            json: json string
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """deserialize json string

        Args:
            list_objs (list obj): json string
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"

        dict_list = []
        for obj in list_objs:
            dict_list.append(obj.to_dictionary())
        json_string = cls.to_json_string(dict_list)

        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Deserialize s (a str, bytes or bytearray instance
        containing a JSON document) to a Python object.

        Args:
            json_string (json string): json string

        Returns:
            obj: py object
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Dictionary to Instance
        To use the update method to assign all attributes, you
        must create a “dummy” instance before:

    Create a Rectangle or Square instance with “dummy” mandatory
    attributes (width, height, size, etc.)
    Call update instance method to this “dummy” instance to apply
    your real value

        Returns:
            obj: returns an instance with all attributes
            already set
        """
        if cls.__name__ == "Square":
            dummy_obj = cls(1)
        if cls.__name__ == "Rectangle":
            dummy_obj = cls(1, 1)
        dummy_obj.update(**dictionary)
        return dummy_obj

    @classmethod
    def load_from_file(cls):
        """File to instances

        Returns:
            obj list: a list of instances:
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_str = file.read()
                obj_dicts = cls.from_json_string(json_str)
                obj_list = []
                for obj in obj_dicts:
                    instance = cls.create(**obj)
                    obj_list.append(instance)
                return obj_list
        except FileNotFoundError:
            return []
    # def load_from_file(cls):
    #     filename = cls.__name__ + ".json"
    #     try:
    #         with open(filename, "r") as file:
    #             return [cls.create(**obj_dict)
    #                     for obj_dict in cls.from_json_string(file.read())]
    #     except FileNotFoundError:
    #         return []

    # @classmethod
    # def load_from_file_csv(cls):
    #     """serializes in CSV

    #     Returns:
    #         obj: csv to py object
    #     """
    #     objs = []
    #     filename = cls.__name__ + ".csv"
    #     with open(filename, 'r', newline='') as f:
    #         reader = csv.reader(f)
    #         for row in reader:
    #             if cls.__name__ == "Rectangle":
    #                 dic = {"id": int(row[0]),
    #                        "width": int(row[1]),
    #                        "height": int(row[2]),
    #                        "x": int(row[3]),
    #                        "y": int(row[4])}
    #             if cls.__name__ == "Square":
    #                 dic = {"id": int(row[0]),
    #                        "size": int(row[1]),
    #                        "x": int(row[2]),
    #                        "y": int(row[3])}
    #             o = cls.create(**dic)
    #             objs.append(o)
    #     return objs

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes from CSV

        Returns:
            list: List of instances of the class.
        """
        objs = []
        filename = cls.__name__ + ".csv"

        field_mapping = {
            "Rectangle": ["id", "width", "height", "x", "y"],
            "Square": ["id", "size", "x", "y"]
        }

        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                obj_dict = {}
                for field_name, value in zip(field_mapping[cls.__name__], row):
                    obj_dict[field_name] = int(value)

                o = cls.create(**obj_dict)
                objs.append(o)
        return objs

    # @classmethod
    # def save_to_file_csv(cls, list_objs):
    #     """deserializes in CSV

    #     Args:
    #         list_objs (_type_): _description_
    #     """
    #     filename = cls.__name__ + ".csv"
    #     with open(filename, 'w', newline='') as f:
    #         writer = csv.writer(f)
    #         for o in list_objs:
    #             if cls.__name__ == "Rectangle":
    #                 writer.writerow([o.id, o.width, o.height, o.x, o.y])
    #             if cls.__name__ == "Square":
    #                 writer.writerow([o.id, o.size, o.x, o.y])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes to CSV

        Args:
            list_objs (list): List of instances of the class.
        """
        filename = cls.__name__ + ".csv"

        field_mapping = {
            "Rectangle": ["id", "width", "height", "x", "y"],
            "Square": ["id", "size", "x", "y"]
        }

        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for o in list_objs:
                row = [getattr(o, field_name)
                       for field_name in field_mapping[cls.__name__]]
                writer.writerow(row)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares

        Args:
            list_rectangles (list): rectangle
            list_squares (list): square
        """
        # Set bg color
        bg_colour = ("#FAE392")

        # List of colors for shapes
        shape_colors = ["red", "green", "blue", "orange",
                        "purple", "pink", "yellow", "brown",
                        "cyan", "magenta, lavender"]

        screen = turtle.Screen()
        # Set the background color
        screen.bgcolor(bg_colour)
        screen.title("Let's draw it!")  # Set the window title

        turtle.shape("turtle")  # Set the pen shape to a turtle
        turtle.pensize(3)

        # Draw Rectangles
        random_color = random.choice(shape_colors)
        turtle.color("#1A5D1A")
        for idx, rectangle in enumerate(list_rectangles):
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            # Set the fill color for rectangles
            turtle.fillcolor(random_color)
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rectangle.width)
                turtle.left(90)
                turtle.forward(rectangle.height)
                turtle.left(90)
            turtle.end_fill()

        # Draw Squares
        random_color = random.choice(shape_colors)
        turtle.color("#1A5D1A")
        for idx, square in enumerate(list_squares):
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            # Set the fill color for squares
            turtle.fillcolor(random_color)
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)
            turtle.end_fill()

        turtle.hideturtle()
        # Allow the window to close on click
        turtle.exitonclick()

        turtle.done()
