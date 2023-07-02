#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(type(float('NaN')))
print(add_integer(1, 2 + 5j))
print(add_integer(1.1, 2))
print(add_integer(4.11, -1.999))
try:
    print(add_integer(-95.1, 98.999))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
