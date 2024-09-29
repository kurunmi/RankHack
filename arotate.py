def rotate(nums, k):
    size = len(nums)
    return nums[size-k:] + nums[:size - k]

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8,9,0,11,12,23,34,45,56,67,78,89,90]
    k = 7
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(rotate(nums, k))