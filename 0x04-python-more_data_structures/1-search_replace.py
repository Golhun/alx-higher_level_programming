#!/usr/bin/python3


def search_replace(my_list, search, replace):
    for item in my_list:
        new_list = []
        if my_list[item] == search:
            my_list[item] = replace
            new_list.append(item)
        elif my_list[item] != search:
            my_list[item] = item
            new_list.append(item)
    return new_list
