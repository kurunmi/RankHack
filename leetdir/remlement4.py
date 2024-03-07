def remlement(nums):
    nums = list(sorted((set(nums))))
    print(nums)
    return len(nums)

if __name__ == '__main__':
    nums = [1, 1, 2]
    nums1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    remlement(nums)
