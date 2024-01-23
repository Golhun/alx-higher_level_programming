#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        start = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            start += 1
        print()
        return start
    except IndexError:
        print()
        return start
