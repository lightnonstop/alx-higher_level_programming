#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        ps_number = -number
    else:
        ps_number = number
    ld = ps_number % 10
    print("{:d}".format(ld), end="")
    return ld
