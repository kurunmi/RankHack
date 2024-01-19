#!/usr/bin/python3

def reach(nums):
    i = 0
    stride_count = 0
    stride_max = 0
    stride_end = 0
    final = len(nums) - 1
    if len(nums) == 1:
        return stride_count
    while i <= final:
        val = nums[i]
        if i == 0:
            stride_end = val
            if val == final:
                return 0
            print(i, stride_count, stride_end, val, myreach, final)
            i += 1
        myreach = val + i
        print(i, stride_count, stride_end, val, myreach,  final)
        if i > stride_end:
            stride_count += 1
            stride_end = val + i
        print(i, stride_count, stride_end, val, myreach, final)
        if myreach >= final:
            return stride_count + 1
        i += 1


if __name__ == '__main__':
    print(reach([2,3,1,1,4]))
    #print(reach([2,3,0,1,4]))
    #print(reach([1,2]))
    #print(reach([3,4,3,1,0,7,0,3,0,2,0,3]))
    #print(reach([1,1,1,1]))



