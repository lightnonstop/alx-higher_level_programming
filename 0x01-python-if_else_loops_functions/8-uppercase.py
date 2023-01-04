#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        upp = str[i]
        if ord(upp) >= 97 and ord(upp) <= 122:
            upp = chr(ord(upp) - 32)
        print("{}".format(upp), end="")
    print(end="\n")
