def votalgo(nums):
    nums = sorted(nums)
    return nums[len(nums)//2]

if __name__ == '__main__':
    nums = [1,2,3,5,5,5,5,5,5,5,5,54,4,4,4]
    print(votalgo(nums))

