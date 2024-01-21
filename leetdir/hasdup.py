def hasdup(nums, k):
    numdict = {}
    for index in range(len(nums)):
        if nums[index] in numdict and abs(index - numdict[nums[index]]) <= k:
            return True
        numdict[nums[index]] = index
    return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    k = 3
    nums1 = [1, 0, 1, 1]
    k1 = 1
    nums2 = [1, 2, 3, 1, 2, 3]
    k2 = 2
    nums3 = [1,7,3,9,13,12,1, 3, 1]
    k3 = 3
    print(hasdup(nums3, k3))