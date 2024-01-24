import datetime

def memo_sqrt(nums):
    memo = {}
    for num in nums:
        mytime = datetime.datetime.now()
        if num not in memo:
            output = num ** num
            memo[num] = output
        else:
            output = memo[num]
        print(str(num).ljust(6), ':', datetime.datetime.now() - mytime)




if __name__ == '__main__':
    nums = [55, 33, 13312, 55, 17175, 172, 33, 173, 13312, 44, 55,
            173, 17175, 13313, 13312, 13312, 55, 33, 172, 13312]
    memo_sqrt(nums)
