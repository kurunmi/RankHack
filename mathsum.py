def twoSum(nums, target):
    checked = {}
    for index in range(len(nums)):
        if (target - nums[index]) in checked:
            return [index, checked[target - nums[index]]]
        checked[nums[index]] = index

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    nums1 = [3, 2, 4]
    target1 = 6
    nums2 = [3, 3]
    target2 = 6
    print(twoSum(nums2, target2))