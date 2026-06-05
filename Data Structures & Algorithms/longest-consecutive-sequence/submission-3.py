"""


"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if (len(nums) == 0): return 0

        maxx = cur = 1

        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                cur += 1
            elif nums[i + 1] == nums[i]:
                continue
            else:
                cur = 1
            maxx = max(maxx, cur)
        
        return maxx

