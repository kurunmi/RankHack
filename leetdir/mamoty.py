def maxProfit(prices):
    pmin = prices[0]
    pmax = 0
    mprofit = 0
    for i in range(len(prices)):
        if prices[i] < pmin:
            pmin = pmax = prices[i]
        elif prices[i] > pmax:
            pmax = prices[i]
            mprofit = max((pmax - pmin), mprofit)
    return mprofit




if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    prices =[7,6,4,3,1]
    print(maxProfit(prices))