#!/usr/bin/python3
import copy

def miniMaxSum(arr):
    result = set()
    sums = []
    for x in range(len(arr)):
        tmp_sum =0
        tmp_arr = copy.deepcopy(arr)
        tmp_arr.pop(x)
        tmp_sum = sum(tmp_arr)
        sums.append(tmp_sum)
        result.add(tuple(tmp_arr))
    print(min(sums), max(sums))

if __name__ == '__main__':
    myarr = [1, 3, 5, 7, 9]
    result = miniMaxSum(myarr)
