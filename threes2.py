def threeSum(nums):
    nums = sorted(nums)
    result = []
    posl = []
    posd = {}
    negl = []
    negd = {}
    zeroes = []
    found = set()

    for num in nums:
        if num > 0:
            posl.append(num)
            if num in posd:
                posd[num] += 1
            else:
                posd[num] = 1
        elif num < 0:
            negl.append(num)
            if num in negd:
                negd[num] += 1
            else:
                negd[num] = 1
        elif num == 0:
            zeroes.append(0)

    if len(zeroes) >= 3:
        found.add((0, 0, 0))

    for p in posl:
        if zeroes and p * -1 in negd:
            found.add((p, 0, p * -1))
        if p % 2 == 0 and (p//2) * -1 in negd and negd[(p//2) * -1] >= 2:
            found.add((p, p//2 - 1, p//2 - 1))
        for n in negl:
            if abs(n) > (p // 2):
                break
            if p - abs(n) in negd:
                found.add((p, n, p-abs(n)))

    posl.reverse()
    negl.reverse()

    for n in negl:
        if n % 2 == 0 and abs(n)//2 in posd and posd[abs(n)//2] >= 2:
            found.add((n, abs(n//2), abs(n//2)))
        for p in posl:
            if p >= (abs(n) // 2):
                break
            if abs(n) - p in posd:
                found.add((n, p, abs(n) - p))
                print(found)

    for item in found:
        result.append([item[0], item[1], item[2]])

    return result

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    nums1 = [0, 0, 0]
    nums2 = [1,1,-2]
    nums3 = [-1,0,1,2,-1,-4]
    nums4 = [1,0,1,-2,-1,4]
    nums5 = [1,1,-2]
    print(threeSum(nums4))


