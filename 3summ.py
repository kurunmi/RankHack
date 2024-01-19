#!/usr/bin/python3

def minSubarraylen(targ, lst):
    res, mysum, index = len(lst)+1, 0, 0
    if sum(lst) < targ:
        return 0
    for r, n in enumerate(lst):
        mysum += n
        while mysum >= targ and index <= r:
            res = min(res, r-index+1)
            mysum -= lst[index]
            index += 1

    return res




if __name__ == '__main__':
    arr1 = [-5, -7, 1, 1, 1, 0,0,0,-1, -1, -1, 2]
    arr2 = [2,3,1,2,4,3]
    print( minSubarraylen(7, arr2))