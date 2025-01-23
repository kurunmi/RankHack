def movezeroes(nums):
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1
    while index < len(nums):
        nums[index] = 0
        index += 1
    return nums


if __name__ == '__main__':
    print(movezeroes([0,1,2,0,4,5,0,6,7]))