def removeElement(nums, val):
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return nums, index


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    nums1 = [0, 1, 2, 2, 3, 0, 4, 2]
    val1 = 2
    print(removeElement(nums1, val1))