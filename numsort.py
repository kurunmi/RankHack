def removeElement(nums, val):
    #nums = sorted(nums)
    count = 0
    mylen = len(nums)
    last = mylen
    index = 0
    while index < last:
        if nums[index] == val:
            nums.pop(index)
            index -= 1
            last -= 1
        else:
            count += 1
        index += 1
    print(nums)
    return count

if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    #nums = [0, 1, 2, 2, 3, 0, 4, 2]
    #val = 2
    print(removeElement(nums, val))
