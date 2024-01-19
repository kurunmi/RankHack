#!/usr/bin/python3

def arrayshft(nums, k):
    shift = (k - len(nums)) % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

if __name__ == '__main__':
    print(arrayshft([1,2,3,4,5,6,7], 3))