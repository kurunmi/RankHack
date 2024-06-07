def threeSum(nums):
    nums = sorted(nums)
    result = []

    size = len(nums)
    inner_start = 0
    while inner_start < size - 2:
        inner_nums = nums[inner_start:]
        nums_start = 0
        nums_mid = 1
        nums_end = len(inner_nums) - 1
        while nums_mid < nums_end:
            nums_sum = inner_nums[nums_start] + inner_nums[nums_end] + inner_nums[nums_mid]
            if nums_sum == 0:
                mylist = [inner_nums[nums_start], inner_nums[nums_end], inner_nums[nums_mid]]
                if mylist not in result:
                    result.append(mylist)
            if nums_sum < 0:
                nums_mid += 1
            else:
                nums_end -= 1
        inner_start += 1
    return result

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    nums1 = [0,0,0]
    print(threeSum(nums1))
