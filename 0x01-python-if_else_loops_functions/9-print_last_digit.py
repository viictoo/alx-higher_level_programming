#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        abs = (number * -1) % 10
    else:
        abs = number % 10
    print(abs, end="")
    return abs
