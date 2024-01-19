#!/usr/bin/python3
import math


def zigzag(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    L = [''] * numRows

    step = 1
    index = 0

    for x in s:
        L[index] += x
        if index == 0:
            step = 1
        elif index == numRows -1:
            step = -1
        index += step

    return ''.join(L)



if __name__ == '__main__':
    s = "abcdefghigklmnopqrstuvwxyz"
    numrows = 5
    print(zigzag(s, numrows))




