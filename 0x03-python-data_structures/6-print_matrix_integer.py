#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    for item in matrix: # get the sublists
        for i,value in enumerate(item): # for every sublist we treat it as a row or an individual list with th enumerate() function
            print("{:d}".format(value), end="") # then we print the values in that list
            if i < (len(item) - 1): # we check if the current element is the last element 
                print(" ", end="") # if it isn't we print a space and keep the next element on the same line with end=""
        print() # we now print a new line before the main for loop runs again
