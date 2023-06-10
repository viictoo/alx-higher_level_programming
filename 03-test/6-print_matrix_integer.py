#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if ((matrix) == [[]]):
        print()
        return
    for row in matrix:
        for i in range(len(matrix)):
            spec = ' '
            if i == len(matrix) - 1:
                spec = ''
            print(f'{row[i]}', end=spec)
        print()
