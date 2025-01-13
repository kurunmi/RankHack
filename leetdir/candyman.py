def candyman(candies, extraCandies):
    maxcandy = sorted(candies)[-1]
    result = []
    for can in candies:
        if can + extraCandies >= maxcandy:
            result.append(True)
        else:
            result.append(False)
    return result


if __name__ == '__main__':
    print(candyman([2,3,5,1,3], 3))