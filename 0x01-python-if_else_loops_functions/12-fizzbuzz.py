#!/usr/bin/env python3
def fizzbuzz():
    for i in range(1, 101):
        if not i % 3 and i % 5:
            print("Fizz", end=" ")
            continue
        elif not i % 5 and i % 3:
            print("Buzz", end=" ")
            continue
        if not (i % 3) and not (i % 5):
            print("FizzBuzz", end=" ")
            continue
        else:
            print(i, end=" ")
