#!/usr/bin/python3
def max_integer(my_list=[]):
    num = my_list[0]
    if not my_list:
        return None
    else:
        for i in range(1, len(my_list)):
            if num < my_list[i]:
                num = my_list[i]
            else:
                continue
    return num
