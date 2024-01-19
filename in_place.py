#!/usr/bin/python3

def makedistinct(nums, val):
    index = 0
    size = len(nums) - 1
    count = 0
    indic = -1
    while index <= size:
        if nums[index] == val:
            nums[index] = 0
            if indic < 0:
                indic = index
        else:
            count += 1
            if indic >= 0:
                nums[indic] = nums[index]
                nums[index] = 0
                indic += 1
        index += 1
    return count


if __name__ == '__main__':
    arr = [1,3,5,3,77,3,5,3,23]
    val = 3
    print(makedistinct(arr, val))
