#!/usr/bin/python3

def candy(ratings):
    n, nums = len(ratings), [1] * len(ratings)

    for x in range(n-1):
        if ratings[x] < ratings[x+1]:
            nums[x+1] = max(1 + nums[x], nums[x+1])

    for x in range(n-2, -1, -1):
        if ratings[x+1] < ratings[x]:
            nums[x] = max(1 + nums[x+1], nums[x])
    return sum(nums)

if __name__ == '__main__':
    print(candy([1,6,10,8,7,3,2]))