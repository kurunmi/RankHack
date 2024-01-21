#!/usr/bin/python3
import numpy

arr = [[11, 2, 4],[4, 5, 6],[10, 8, -12]]

def get_diags(arr):
    size = len(arr[0])
    diag1 = 0
    diag2 = 0
    for iter1 in range(size):
        iter2 = size - (iter1 + 1)
        diag1 += arr[iter1][iter1]
        diag2 += arr[iter1][iter2]
    output = diag1 - diag2
    return (abs(output))



def diagonalDifference(arr):
    pass


print(get_diags(arr))