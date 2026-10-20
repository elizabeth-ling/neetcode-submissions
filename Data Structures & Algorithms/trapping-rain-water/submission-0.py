"""
prefix suffix approach 
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        prefix = [0] * n
        suffix = [0] * n

        maxx = 0
        for i in range(n):
            maxx = max(maxx, height[i])
            prefix[i] = maxx

        maxx = 0
        for i in range(n - 1, -1, -1):
            maxx = max(maxx, height[i])
            suffix[i] = maxx
        
        res = 0
        for i in range(n):
            res += min(prefix[i], suffix[i]) - height[i]

        return res
