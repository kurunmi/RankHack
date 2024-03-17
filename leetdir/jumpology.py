def jump(nums):
    dist = nums[0]
    for index in range(1, len(nums)):
        print(index, dist, nums[index])
        if dist > 0:
            dist -= 1
            dist = max(dist, nums[index])
        else:
            return False
    return True

if __name__ == '__main__':
    nums = [2,0,1,0,4]
    nums1 = [3, 2, 1, 0, 4]
    print(jump(nums1))

