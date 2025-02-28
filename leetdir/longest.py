def longest(nums, k):
    l = t = 0
    ml = 0
    for i in range(len(nums)):
        print(i, nums[i], t, l, ml)
        if nums[i] == 1:
            l += 1
            print(i, nums[i], t, l, ml)
        elif nums[i] == 0:
            ml = max(ml, l)
            t += l
            l = 0
    ml, t = max(ml, l), t + l
    return ml + min(t, k)


if __name__ == '__main__':
    print(longest([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))

