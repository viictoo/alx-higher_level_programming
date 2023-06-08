#!/usr/bin/python3
from sys import argv as av
ac = len(av) - 1
if ac == 0:
    print(f"{ac} arguments.")
elif ac == 1:
    print(f"{ac} argument:")
else:
    print(f"{ac} arguments:")
for i in range(ac):
    print(f'{i + 1}: {av[i+1]}')
