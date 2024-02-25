def numgifts(prices, k):
    total = 0
    num = 0
    for price in sorted(prices):
        total += price
        num += 1
        if total > k:
            return num -1
    return num

if __name__ == '__main__':
    prices = [1,2,3,4]
    k = 7
    p1 = [1, 12, 5, 111, 200, 1000, 10]
    k1 = 50
    print(numgifts(p1, k1))