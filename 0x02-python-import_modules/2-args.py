#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    n_len = len(argv) - 1
    if n_len == 0:
        print("{:d} arguments.".format(n_len))
    else:
        if n_len == 1:
            print("{:d} argument:".format(n_len))
        else:
            print("{:d} arguments:".format(n_len))
        for i in range(1, len(argv)):
            print("{:d}: {}".format(i, argv[i]))
