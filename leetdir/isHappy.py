def isHappy(n):
    if n == 1:
        return True
    prev_sums = {}
    while 1:
        nums = list(str(n))
        n = 0
        for num in nums:
            n += int(num)**2
        if n in prev_sums:
            return False
        prev_sums[n] = 0
        if n == 1:
            return True


if __name__ == '__main__':
    nums = 133
    print(isHappy(nums))
