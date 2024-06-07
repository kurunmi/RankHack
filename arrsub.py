def subArray(target, nums):
    total = 0
    smallest = len(nums) + 1
    start = 0
    sl = 0
    for index in range(len(nums)):
        total += nums[index]
        while total >= target:
            smallest = min(smallest, index - start+1)
            total -= nums[start]
            start += 1
    return smallest


if __name__ == '__main__':
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    print(subArray(target, nums))

