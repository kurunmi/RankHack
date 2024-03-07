def remlement(nums):
    count = len(nums)
    index = 0
    next_index = index + 1
    current_null = 0
    for i in range(len(nums)):
        while next_index < count and nums[index] == nums[next_index]:
            count -= 1
            nums[next_index] = ''
            next_index += 1
        nums[index + 1], nums[next_index] = nums[next_index], nums[index+1]
        index += 1
        next_index += 1
    return count, nums

if __name__ == '__main__':
    nums = [1, 1, 2]
    nums1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(remlement(nums1))

