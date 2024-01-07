#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    for item in matrix:
        for i, value in enumerate(item):
            print("{:d}".format(value), end="")
            if i < (len(item) - 1):
                print(" ", end="")
        print()
