#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score = 0
    weight = 0
    for i in range(len(my_list)):
        score += my_list[i][0] * my_list[i][1]
        weight += my_list[i][1]
    weighted_average = score / weight
    return weighted_average
