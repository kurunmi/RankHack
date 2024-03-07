def remlement(nums):
    count = len(nums)
    index = 0
    comparator = index + 1
    for checker in range(1, len(nums)):
        if nums[checker] != nums[index]:
            nums[checker], nums[comparator] = nums[comparator], nums[checker]
            index = comparator
            comparator += 1
    for x in range(index +1, len(nums)):
        nums[x] = ''
    print(nums)
    return len(set(nums))



if __name__ == '__main__':
    nums = [1, 1, 2]
    nums1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    remlement(nums1)
