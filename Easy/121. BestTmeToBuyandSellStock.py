"""
121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        min_price = prices[0] # initializing the min price to the price on the first day
        max_profit = 0 # initializing the max profit to 0

        for price in prices:
            if price < min_price:
                min_price = price # update the min price if a lower price is encountered
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit