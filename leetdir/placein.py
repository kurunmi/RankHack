

def placein(nums, k):
    print(nums)
    a = len(nums)
    a %= 1
    nums[:] = nums[k:] + nums[:k]
    return nums



if __name__ == '__main__':
    nums = [0,0,1,1,2,2,2,2,3,3,5,5,5,5,6,6,7,7]
    print(placein(nums, 12))