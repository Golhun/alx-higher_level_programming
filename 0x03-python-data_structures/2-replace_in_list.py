#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > (len(my_list) - 1):
        return my_list
    elif idx > 0 and idx <= (len(my_list)):
        my_list[idx] = element
        return my_list


if __name__ == "__main__":
    replace_in_list()
