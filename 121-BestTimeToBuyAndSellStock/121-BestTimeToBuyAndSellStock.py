# Last updated: 7/10/2025, 11:58:22 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prices[0]
        for x in prices[1:]:
            if buy_price > x:
                buy_price = x
            z = x - buy_price
            profit = max(profit, z)
        return profit

                