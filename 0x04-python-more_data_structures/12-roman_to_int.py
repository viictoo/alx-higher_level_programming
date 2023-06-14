#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10,  "I": 1, "V": 5}

    last = 0
    total = 0
    for i in roman_string[::-1]:
        if i not in roman:
            return 0
        if roman[i] < last and last:
            total -= roman[i]
        else:
            total += roman[i]
        last = roman[i]
    return total
