def twolements(nums):
    index = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[index - 1]:
            nums[index] = nums[i]
            index += 1
        elif nums[i] != nums[index - 2]:
            nums[index] = nums[i]
            index += 1
    return index


if __name__ == '__main__':
    nums = [1, 1, 2]
    nums1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4]
    twolements(nums1)