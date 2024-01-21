#!/usr/bin/python3

def buysell(prices):
    maxbuy = prices[0]
    maxsell = maxbuy
    maxearn = 0
    if len(prices) < 1:
        return 0
    earnings = 0
    for pip in prices:
        print(pip, earnings, maxbuy, maxearn)
        if pip <= maxbuy:
            maxbuy = pip
        if pip > maxbuy:
            maxearn += (pip - maxbuy)
            maxbuy = pip
            if earnings > maxearn:
                maxearn = earnings
    return maxearn


if __name__ == '__main__':
    print(buysell([]))
