#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    prod = 0
    if my_list:
        for elem in my_list:
            prod += elem[0] * elem[1]
            sum += elem[1]
        return prod / sum
    else:
        return 0
