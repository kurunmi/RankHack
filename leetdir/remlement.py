def remlement(nums, val):
    count = len(nums)
    mylen = count -1
    index1 = mylen
    while mylen >= 0:
        if nums[mylen] == val:
            count -= 1
            nums[mylen] = ''
            if index1 != mylen:
                nums[mylen], nums[index1] = nums[index1], nums[mylen]
                index1 -= 1
            else:
                index1 -= 1
        mylen -= 1
    return count

if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    print(remlement(nums, val))
