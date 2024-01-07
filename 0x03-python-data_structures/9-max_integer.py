#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list == []:
        return None
    elif my_list != []:
        my_list.sort()
        last_index = (len(my_list) - 1)
        return my_list[last_index]
    