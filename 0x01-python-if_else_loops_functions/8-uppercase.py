#!/usr/bin/python3
def uppercase(str):
    for w in str:
        if ord(w) >= 97 and ord(w) < 123:
            w = ord(w) - 32
        else:
            w = ord(w)
        print(chr(w), end="")
    print()
