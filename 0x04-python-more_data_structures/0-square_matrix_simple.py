#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """"""" a function that computes the square value of all integers of a matrix """""""
    matrixx = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix[i])):
            temp.append(matrix[i][j] * matrix[i][j])
        matrixx.append(temp)
    return matrixx
