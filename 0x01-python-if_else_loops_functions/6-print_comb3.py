#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i >= j:
            continue
        if j == 1:
            print("{:d}{:d}".format(i,  j), end="")
        else:
            print(", {:d}{:d}".format(i,  j), end="")
print(end="\n")
