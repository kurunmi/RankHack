def rotate(nums, k):
    l = len(nums)
    if l < 2:
        return nums
    k %= l
    return nums[-k:] + nums[:-k][:]

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(rotate(nums, k))