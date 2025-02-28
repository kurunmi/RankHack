def longest(nums):
    l = 0
    k = 1
    count = 0
    for r in range(len(nums)):
        if k:
            if nums[r] == 1:
                count += 1
            elif nums[r] == 0 and k:
                k -= 1
                count += 1




if __name__ == '__main__':
    a = [1,1,1,0,0,0,1,1,1,1,0]
    b = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    c = [1,1,0,1]
    d = [0,1,1,1,0,1,1,0,1]
    print(longest(d))

