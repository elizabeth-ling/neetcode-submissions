"""
height = [1,7,2,5,4,7,3,6]

l = 0
r = 7
volume = (r - 7) * min(l, r)

"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            v = (r - l) * min(heights[l], heights[r])
            res = max(res, v)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        
        return res

