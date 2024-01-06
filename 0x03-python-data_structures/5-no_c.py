#!/usr/bin/python3


def no_c(my_string):
    my_string = [
        i for i in my_string if not (
            i == 'c' or i == 'C'
            )
        ]
    string = "".join(my_string)
    return string


if __name__ == "__main__":
    no_c()
