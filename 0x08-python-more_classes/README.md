0x0

# 8 More classes tasks in Python

---summary---
this project dives into the following concepts using a Rectagle class
init, repr, str, doc, minimal class, attributes, methods, abstractions, encapsulation, information hiding, public vs protected attributes, Destructor

# Rectangle Class

The `Rectangle` class is a Python implementation of a rectangle object. It allows you to create rectangle instances with specified width and height, perform various operations on rectangles, and retrieve information about them.

## Usage

To create a rectangle instance, initialize it with the desired width and height:

```python
rectangle = Rectangle(width, height)
```

You can access the width and height properties of the rectangle using the `width` and `height` attributes, respectively:

```python
rectangle.width
rectangle.height
```

You can also modify the width and height values using the same attributes:

```python
rectangle.width = new_width
rectangle.height = new_height
```

## Methods

### `area()`

The `area()` method calculates and returns the area of the rectangle.

```python
rectangle.area()
```

### `perimeter()`

The `perimeter()` method calculates and returns the perimeter of the rectangle.

```python
rectangle.perimeter()
```

### `__str__()`

The `__str__()` method provides a string representation of the rectangle using the `print_symbol` attribute. It prints the rectangle with the specified symbol, repeated based on the width and height of the rectangle. If either the width or height is 0, it returns an empty string.

```python
print(rectangle)
```

### `__repr__()`

The `__repr__()` method provides a string representation of the rectangle that can be used to recreate a new instance of the rectangle using `eval()`. The string representation follows the format "Rectangle(width, height)".

```python
repr(rectangle)
```

### `__del__()`

The `__del__()` method is called when an instance of the rectangle is deleted. It prints the message "Bye rectangle..." to indicate the deletion of the instance.

### `bigger_or_equal(rect_1, rect_2)`

The `bigger_or_equal()` static method compares two rectangles based on their areas and returns the rectangle with the larger area. If either `rect_1` or `rect_2` is not an instance of the `Rectangle` class, it raises a `TypeError` with an appropriate error message.

```viictoo
Rectangle.bigger_or_equal(rect_1, rect_2)
```

### `square(cls, size=0)`

The `square()` class method returns a new rectangle instance with equal width and height, creating a square. It takes an optional `size` argument that specifies the size of the square. If `size` is not provided, it defaults to 0.

```python
Rectangle.square(size)
```

## Class Attributes

### `number_of_instances`

The `number_of_instances` attribute keeps track of the number of `Rectangle` instances that have been created and not deleted.

### `print_symbol`

The `print_symbol` attribute is a public class attribute that can be set to any type. It is used as the symbol to print the string representation of the rectangle.

## Example

Here's an example of how to use the `Rectangle` class:

```viictoo
# Create rectangle instances
rectangle1 = Rectangle(4, 6)
rectangle2 = Rectangle(3, 3)

# Access width and height attributes
print(rectangle1.width)  # Output: 4
print(rectangle1.height)  # Output: 6

# Calculate area and perimeter
print(rectangle1.area())  # Output: 24
print(rectangle1.perimeter())  # Output: 20

# Print string representation
print(rectangle1)  # Output: ####
                   #         ####
                   #         ####
                   #

 ####

# Get the string representation for recreating a new instance
print(repr(rectangle1))  # Output: Rectangle(4, 6)

# Compare rectangles based on area
larger_rectangle = Rectangle.bigger_or_equal(rectangle1, rectangle2)

# Create a square
square = Rectangle.square(5)
```

In this example, two rectangle instances are created with different widths and heights. Various operations are performed, such as retrieving width and height, calculating area and perimeter, printing the string representation, getting the representation for recreating a new instance, comparing rectangles based on area, and creating a square.

## License

This project is licensed under the [MIT License](LICENSE).

Please note that this README assumes basic familiarity with Python and object-oriented programming concepts.
