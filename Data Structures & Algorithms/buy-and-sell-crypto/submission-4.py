
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_buy = prices[0]

        for price in prices:
            res = max(res, price - min_buy)
            min_buy = min(min_buy, price)
        
        return res
