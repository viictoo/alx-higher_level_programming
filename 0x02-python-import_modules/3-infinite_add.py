#!/usr/bin/python3
from sys import argv as av

if __name__ == '__main__':
    result = 0
    j = 1
    for i in enumerate(av[1:]):
        result += (int(av[j]))
        j += 1
    print(result)
