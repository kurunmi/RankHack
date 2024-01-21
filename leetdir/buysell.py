#!/usr/bin/python3

def busell(prices):
    buyindex = 0
    sellindex = len(prices)-1
    bestbuy = prices[buyindex]
    bestsell = prices[sellindex]
    if len(prices) == 1:
        return 0
    if len(prices) > 2:
        while buyindex < sellindex:
            print(buyindex, sellindex)
            buyindex += 1
            sellindex -= 1
            if bestbuy > prices[buyindex]:
                bestbuy = prices[buyindex]
            if bestsell < prices[sellindex]:
                bestsell = prices[sellindex]
            return bestsell - bestbuy
        return 0


if __name__ == '__main__':
    print(busell([2,1]))

    print(int(None))
