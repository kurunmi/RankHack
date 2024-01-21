#!/usr/bin/python3
import random


def newbfs(nums):
    stride = 0
    stride_end = 0
    reach = 0
    end = len(nums) - 1
    if len(nums) == 1:
        return stride
    for i in range(end):
        if (i + nums[i]) > reach:
            reach = (i + nums[i])
        if reach >= end:
            stride += 1
            return stride
        if i == stride_end:
            stride += 1
            stride_end = reach
        i += 1


if __name__ == '__main__':
    #print(newbfs([2,3,1,1,4]))
    #print(newbfs([2,3,0,1,4]))
    #print(newbfs([1,2]))
    #print(newbfs([3,4,3,1,0,7,0,3,0,2,0,3]))
    #print(newbfs([0]))
    myset = set()
    for i in range(int(random.random()*100)):
        myset.add(int(random.random() *100))
    print(myset)
    print(13 in myset)
    randex = random.randrange(0,len(myset))
    print(randex)
    print(list(myset)[randex])


