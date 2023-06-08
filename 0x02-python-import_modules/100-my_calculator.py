#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv as av

if __name__ == "__main__":
    if len(av) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = av[2]
    a = int(av[1])
    b = int(av[3])

    if op == '+':
        print(f"{a} {op} {b} = {add(a,b)}")
    elif op == '-':
        print(f"{a} {op} {b} = {sub(a,b)}")
    elif op == '*':
        print(f"{a} {op} {b} = {mul(a,b)}")
    elif op == '/':
        print(f"{a} {op} {b} = {div(a,b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
