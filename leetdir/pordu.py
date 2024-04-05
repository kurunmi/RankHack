def productExceptSelf(nums):
    zeros = 0
    nonzerosum = 1
    final = []
    if len(nums) == 1 and nums[0] == 0:
        return nums

    for num in nums:
        if num == 0:
            zeros += 1
        if zeros > 1:
            final = [0] * len(nums)
            return final
        nonzerosum *= num if num != 0 else 1
    for num in nums:
        if zeros:
            if num == 0:
                final.append(nonzerosum)
            else:
                final.append(0)
        else:
            final.append(nonzerosum // num)
    return final



if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    num1 = [5, 0, 7, 0]
    print(productExceptSelf(nums))