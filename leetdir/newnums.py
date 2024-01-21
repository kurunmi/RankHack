#!/usr/bin/python3

def newsums(nums):
    print(nums)
    nums = sorted(nums)
    triplets = []
    end = len(nums) - 1
    start = 0
    while end > start:
        inner = nums[start+1:end]
        for val in inner:
            inlst = sorted([nums[start], nums[end], val])
            if 4 in inlst or -4 in inlst or nums[end] == 4:
            if nums[start] + nums[end] + val == 0 and inlst not in triplets:
                triplets.append(inlst)
        end -= 1
    return triplets


if __name__ == '__main__':
    arr1 = [-5, -7, 1, 1, 1, 0,0,0,-1, -1, -1, 2]
    arr3 = [0,0,0,0,0,0]
    arr2 = [-1,0,1,2,-1,-4]
    arr4 = [-2,-1, -1, 0,1,1,2]
    arr5 = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    print(newsums(arr5))