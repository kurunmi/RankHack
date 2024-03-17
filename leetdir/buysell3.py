def maxprofit(prices):
    bucket = 0
    last_price = prices[0]
    for price in prices:
        if last_price < price:
            bucket += price - last_price
        last_price = price
    return bucket

if __name__ == '__main__':
    prices = [7,6,4,3,2,1]
    maxprofit(prices)
