#!/usr/bin/python

def mrgsort(nums1, m, nums2, n):
    tot = len(nums1) - 1
    while m and n:
        if nums1[m] >= nums2[n]:
            nums1[tot] = nums1[m]
            m -= 1
        else:
            nums1[tot] = nums2[n]
            n -= 1
        tot -= 1
    if n:
        nums1[0:n-1] = nums2[0:n-1]
    return nums1


def removeElement(nums, val):
    index = 0
    for x in range(len(nums) -1):
        if nums[x] != val:
            nums[index] = nums[x]
            index += 1
    return index, nums

def removeDuplicates(nums):
    uniq = 0
    for index in range(1, len(nums)):
        if nums[uniq] != nums[index]:
            nums[uniq + 1] = nums[index]
            uniq += 1
    return nums


def removeDuplicates2(nums):
    if len(nums) == 2:
        return nums
    uniq = 1
    for index in range(2, len(nums)):
        if nums[index] != nums[index - 2]:
            nums[uniq] = nums[index]
            uniq += 1
    return nums

def rotateArray(nums, k):
    l = len(nums)
    if k == l or l < 2:
        return nums
    k %= l
    nums [:] = (nums[-k:] + nums[:-k])
    return nums


def maxProfit(nums):
    mprof = 0
    minp = nums[0]
    for x in nums:
        if x > minp:
            mprof += x - minp
        minp = x
    return mprof


def canJump(jumps):
    jmp = jumps[0]
    for x in jumps:
        if jmp <= 0:
            return False
        jmp -= 1
        jmp = max(jmp, x)
    return True


def maxJump(prices):
    current = prices[0]
    l = len(prices)
    maxjmp = 0
    jmp = 0
    for x in range(l):
        maxjmp = max(maxjmp, x + prices[x])
        if maxjmp >= l:
            return jmp + 1
        if x == current:
            jmp += 1
            current = prices[x+1]






if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5]
    prices = [4,1,1,0, 7]
    val = 3
    #print(rotateArray(nums, 7))
#    print(canJump(prices))
    print(prices)
    print(prices[0:len(prices)])
    print(len(prices))
    print(max(prices))


