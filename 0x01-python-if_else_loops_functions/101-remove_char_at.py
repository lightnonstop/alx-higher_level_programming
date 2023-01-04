#!/usr/bin/python3
def remove_char_at(str, n):
    n_str = ""
    for i in range(0, len(str)):
        if i != n:
            n_str = n_str + str[i]
    return n_str
