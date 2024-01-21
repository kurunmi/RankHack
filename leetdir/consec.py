def longestConsecutive(nums):
    if len(nums) ==0:
        return 0
    #nums = sorted(list(set(nums)))
    nums = sorted(nums)
    print(nums)
    max_count = 0
    count = 0
    last_diff = False
    diff = False
    for index in range(len(nums)):
        count += 1
        if index - 1 < 0:
            pass
        else:
            diff = nums[index] - nums[index-1]
        if diff is not False and not diff:
            count = 1
        elif last_diff is not False and last_diff != diff:
            count = 2
            diff = nums[index] - nums[index-1]
        last_diff = diff
        if count > max_count:
            max_count = count
        print(nums[index], index, last_diff, diff, count)
    return max_count





if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    nums1 = [0,3,7,2,5,8,4,6,0,1]
    nums2 = [-1,-3,-2,0,1, 200,300, 600,500,100,400]
    nums3 = [-3,-2,1,0,2,4,6,100,200,300,400,500,600]
    nums4 = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]
    nums5 = [-8,-4,9,9,4,6,1,-4,-1,6,8]
    nums6 = [0,0,0,0,0]
    print(longestConsecutive(nums5))





