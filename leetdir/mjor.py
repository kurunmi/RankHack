
def majorityElement(nums):
    return sorted(nums)[len(nums)//2]


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 3, 5, 5, 5, 5,5,5]
    print(majorityElement(nums))