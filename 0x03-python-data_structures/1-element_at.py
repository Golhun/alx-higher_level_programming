#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > (len(my_list) - 1):
        return None
    elif idx > 0 and idx <= (len(my_list) - 1):
        for element in my_list:
            if element == idx:
                return element


if __name__ == "__main__":
    element_at()
