#!/usr/bin/python3

import collections
import time


def get_uniq(arr):
    items = {}
    dupes = {}
    print(len(arr))
    while arr:
        item = arr.pop()
        if item in items:
            dupes[item] = ''
        if item not in items:
            items[item] = ''
    print(len(dupes), len(items))
#    return sorted(dupes.keys())



if __name__ == '__main__':
    #arr = [33, 33, 43, 1, 2, 3, -33, -33,  4, 5, 4, 6, 7, 123, 44, 2, 3, 55, 3, 55, 44, 7]
    arr = [33, 33, 43, 43, 43, 6, 42]
    print(get_uniq(arr))