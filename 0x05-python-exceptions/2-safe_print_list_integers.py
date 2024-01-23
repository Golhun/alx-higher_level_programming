#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    start = 0
    try:
        for item in my_list[:x]:
            if type(item) == int:
                print("{:d}".format(item), end="")
                start += 1
        print()
    except IndexError:
        print()
    return start
