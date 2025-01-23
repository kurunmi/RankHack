def maxOps(nums, k):
    #nums = sorted(nums)
    x = 0
    y = len(nums) -1
    count = 0
    newnums = {}
    for i in nums:
        if i not in newnums:
            newnums[i] = 0
        newnums[i] += 1
    for i in nums:
        if newnums[i] > 1:
            newnums[i] -= 1
            print(newnums, i)
            if k - i  in newnums and newnums[k - i] > 0:
                count += 1
                newnums[k - i] -= 1
        print(newnums, i, count)
    return count





if __name__ == '__main__':
    print(maxOps([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3))



