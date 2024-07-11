"""You are given an array prices where prices[i] is the
price of a given stock on the i th day.
You want to maximize
your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.
Return the max profit you can achieve from this transaction.
If you cannot achieve any profit, return 0."""


def max_profit(prices):
    left, right = 0, 1
    max_pro = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_pro = max(max_pro, profit)
        else:
            left = right
        right += 1
    return max_pro


priceList = [7, 1, 5, 3, 6, 4]
print(max_profit(priceList))
