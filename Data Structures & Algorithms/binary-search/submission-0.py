"""
binary search

EXAMPLE
Input: nums=[-1,0,2,4,6,8], target=4
l = 0, r = 5
n = 2
nums[n] == 2
2
"""

class Solution:
    def binarySearch(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l > r:
            return -1

        n = l + (r - l) // 2

        if nums[n] == target:
            return n
        if nums[n] > target:
            return self.binarySearch(l, n - 1, nums, target)
        
        return self.binarySearch(n + 1, r, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(0, len(nums) - 1, nums, target)

        