#!/usr/bin/python3
alpha = 97
while alpha <= 122:
    if alpha == 101 or alpha == 113:
        alpha += 1
        continue
    print("{:c}".format(alpha), end="")
    alpha += 1
