def removeDuplicates(nums):
    index = 2
    for i in range(len(nums), 2):
        if nums[i] != nums[index - 1] and nums[i] != nums[index - 2]:
            nums[index] = nums[i]
            index += 1
    return index

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    print(removeDuplicates(nums))