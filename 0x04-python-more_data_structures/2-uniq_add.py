#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    n_set = set(my_list)
    for x in n_set:
        total += x
    return total
