#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_row = []
    for i in matrix:
        new_item = []
        for item in i:
            new_item.append(item ** 2)
        new_row.append(new_item)
    return new_row
