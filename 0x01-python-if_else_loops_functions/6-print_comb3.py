#!/usr/bin/python3
for a in range(10):
    for b in range(1, 10):
        if ((10 * a + b) > (10 * b + a)) or a == b:
            continue
        if a == 8 and b == 9:
            print("{}{}".format(a, b))
            break
        print("{}{}, ".format(a, b), end="")
