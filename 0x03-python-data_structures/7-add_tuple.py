#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    arr = []
    if len(tuple_a) > len(tuple_b):
        Longest = len(tuple_a)
    else:
        Longest = len(tuple_b)
    for i in range(Longest):
        if i > len(tuple_a) - 1:
            arr.append(tuple_b[i])
        elif i > len(tuple_b) - 1:
            arr.append(tuple_a[i])
        else:
            arr.append(tuple_a[i] + tuple_b[i])
    return tuple(arr)
