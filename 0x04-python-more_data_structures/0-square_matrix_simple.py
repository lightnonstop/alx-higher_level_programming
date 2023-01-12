#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    arr = []
    for i in range(len(matrix)):
        col = []
        for j in range(len(matrix[i])):
            col.append(matrix[i][j] ** 2)
        arr.append(col)
    return arr
