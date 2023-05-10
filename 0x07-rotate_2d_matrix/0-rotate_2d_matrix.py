#!/usr/bin/python3
""" 2d rotation matrix"""


def rotate_2d_matrix(matrix):
    """ rotate matrix 90 degrees clockwise"""
    n = len(matrix)
    temp = [row[:] for row in matrix]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = temp[n - j - 1][i]
