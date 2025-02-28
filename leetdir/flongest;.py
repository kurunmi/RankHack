def longest(nums, k):
    mcount = count = flips = left = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            mcount = max(count, mcount)
        else:
            if flips < k:
                flips += 1
                count += 1
                mcount = max(count, mcount)
            else:
                while nums[left] == 1:
                    left += 1
                    count -= 1
                left += 1
    return mcount


if __name__ == '__main__':
    a = [1,1,1,0,0,0,1,1,1,1,0]
    b = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    print(longest(b, 3))

[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]