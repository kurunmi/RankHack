def threeSum(nums):
    nums = sorted(nums)
    freqd = {}
    found = set()
    results = []
    for num in nums:
        if num in freqd:
            freqd[num] += 1
        else:
            freqd[num] = 1

    if 0 in freqd and freqd[0] >= 3:
        results.append([0, 0, 0])

    for item in freqd:
        if item != 0 and freqd[item] >= 2:
            if (-2 * item) in freqd:
                results.append([item, item, -2 * item])
    ilist = sorted(freqd.keys())
    size = len(ilist)
    for i in range(size):
        if ilist[i] == 0:
            break
        for j in range(i+1, size):
            third = -(ilist[i] + ilist[j])
            if third <= ilist[j]:
                break
            if third in freqd:
                print(ilist[i], ilist[j], third)
                results.append([ilist[i], ilist[j], third])
    return results


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))