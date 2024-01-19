#!/usr/bin/python

def inplace(nums):
    k = 0
    zeroes = 0
    for index in nums:
        if k < 2 or nums[k-2] != index:
            nums[k] = index
            k += 1
    print(nums[:k])
    return k


if __name__ == '__main__':
    print(inplace([0,0,1,1,1,1,2,3,3]))


