def buysell(prices):
   # prices = reversed(prices)
    maxi = 0
    maxdelta = 0
    for i in range(len(prices)-1, -1, -1):
        print(maxi, prices[i], maxi - prices[i])
        maxi = max(maxi, prices[i])
        maxdelta = max(maxdelta, maxi - prices[i])
    print(maxi, maxdelta)
    return maxdelta

if __name__ == '__main__':
    princes = [1,2]
    buysell(princes)