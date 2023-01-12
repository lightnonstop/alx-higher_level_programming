#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    d = dict(sorted(a_dictionary.items()))
    for i, j in d.items():
        print(i, end=": ")
        print(j, end="\n")
