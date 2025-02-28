def maxavg(nums, k):
    maxsum = sum(nums[:k])
    l = len(nums)
    for i in range(l-k+1):
        maxsum  = max(maxsum, sum(nums[i:i+k]))
    return maxsum/k





if __name__ == '__main__':
    print(maxavg([5], 1))
