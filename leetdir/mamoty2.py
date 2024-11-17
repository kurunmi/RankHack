def maxProfit(prices):
    pmin = prices[0]
    tprof = 0
    for x in range(len(prices)):
        if prices[x] > pmin:
            tprof += prices[x] - pmin
        pmin = prices[x]
    return tprof

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    p1 = [0,1,2,3,4,5]
    p2 = [5,4,3,2,1]
    p3 = [1,2,3,1,3]
    p4 = [1,1,1,1,1,1]
    p5 = [1]

    print(maxProfit(p5))