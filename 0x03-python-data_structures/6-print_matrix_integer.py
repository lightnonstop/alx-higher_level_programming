#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == len(matrix[i]) - 1 and i == len(matrix) - 1:
                print("{:d}".format(matrix[i][j]), end="")
            elif j == len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]), end="\n")
            else:
                print("{:d}".format(matrix[i][j]), end=" ")
    print()
