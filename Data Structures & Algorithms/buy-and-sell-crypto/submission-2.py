"""
INTUITION:
- sliding window, keep track of current profit and max profit
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, max_profit = 0, 0, 0
        
        while (l <= r and r < len(prices)):
            cur_profit = prices[r] - prices[l]

            max_profit = max(max_profit, cur_profit)
            
            if prices[r] < prices[l]:
                l += 1
            else:
                r += 1

        return max_profit

