#!/usr/bin/python3


def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > (len(my_list) - 1):
        return None
    elif idx in range(0, len(my_list)):
        return my_list[idx]
