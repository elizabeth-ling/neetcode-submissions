"""
binary search 
- l and r pointers
- if nums[m] < nums[r], then min must be between m and r
- else, min must be between l and m 

"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, res = 0, len(nums) - 1, float('inf')

        while l < r:
            m = l + ((r - l) // 2)

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return nums[r]
