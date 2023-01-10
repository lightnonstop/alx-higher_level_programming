#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        num = my_list[0]
        for i in range(1, len(my_list)):
            if num < my_list[i]:
                num = my_list[i]
            else:
                continue
    return num

my_list = []
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
