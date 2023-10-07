#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mtx in matrix:
        for i in mtx:
            print("{:d}".format(i), end=" " if i != mtx[-1] else "")
            print()
