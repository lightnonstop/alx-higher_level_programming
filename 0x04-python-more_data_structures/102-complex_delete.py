#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        keylist = list(a_dictionary.keys())
        valuelist = list(a_dictionary.values())
        position = valuelist.index(value)
        del a_dictionary[keylist[position]]
    return a_dictionary
