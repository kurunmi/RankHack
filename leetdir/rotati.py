def roraty(nums, k):
    l = len(nums)
    if k == l:
        return nums
    k %= l
    return nums[-k:] + nums[:-k]
