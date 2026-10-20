"""
height = [0,2,0,3,1,0,1,3,2,1]
res = 0

l = 0
r = 9
maxL = 0
maxR = 1

maxL - height[l]

"""

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        maxL, maxR = 0, 0

        while l < r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])

            if maxL < maxR:
                res += maxL - height[l]
                l += 1
            else:
                res += maxR - height[r]
                r -= 1

        return res
