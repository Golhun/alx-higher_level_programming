#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for item in range(list_length):
        try:
            num = my_list_1[item]
            de_num = my_list_2[item]
            ans = num / de_num
        except ZeroDivisionError:
            print("division by 0")
            ans = 0
        except TypeError:
            print("wrong type")
            ans = 0
        except IndexError:
            print("out of range")
            ans = 0
        finally:
            new_list.append(ans)

    return new_list
