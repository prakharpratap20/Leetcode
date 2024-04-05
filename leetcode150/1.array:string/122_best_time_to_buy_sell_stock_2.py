"""You are given an integer array prices where prices[i] is the price
of a given stock on the i th day.
On each day, you may decide to buy and/or sell the stock. You can only hold
at most one share of the stock at any time. However, you can buy it then 
immediately and sell it on the same day. 
Find and return the maiximum profit you can achieve."""

def max_profit(prices):
    max_pro = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            max_pro += prices[i] - prices[i-1]

    return max_pro

priceList = [7, 1, 5, 3, 6, 4]

print(max_profit(priceList))
