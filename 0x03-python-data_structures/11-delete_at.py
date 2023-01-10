#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        arr = []
        for i in range(len(my_list)):
            if i != idx:
                arr.append(my_list[i])
            else:
                continue
    my_list[:] = arr[:]
