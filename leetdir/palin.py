#!/usr/bin/python3
import math


def isPalin(s):
    newstr = ""
    for x in s:
        if str.isalnum(x):
            newstr += x.lower()
    if not newstr or len(newstr) < 2:
        return True
    mid = math.floor(len(newstr)/2)
    if len(newstr) % 2 == 0:
        return newstr[:mid] == newstr[mid:][::-1]
    return newstr[:mid] == newstr[mid+1:][::-1]

if __name__ == '__main__':
    print(isPalin("!043XjqjX043!"))