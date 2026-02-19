# You are given an array prices where prices[i] is the price of a stock on day i.
# You want to buy once and sell once to get the maximum profit.

prices = [7,1,5,3,6,4]


def profit(prices):
    min_price = float('inf')
    max_price = 0
    for price in prices:
        if price < min_price:
           min_price = price
        max_price = max(max_price,price - min_price)
    return max_price

result = profit(prices)
print(result)
