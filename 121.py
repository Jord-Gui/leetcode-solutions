# Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        lowest_prev = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            current_price = prices[i]
            if current_price > lowest_prev:
                profit = current_price - lowest_prev
                if profit > max_profit:
                    max_profit = profit
            else:
                lowest_prev = current_price
        return max_profit
