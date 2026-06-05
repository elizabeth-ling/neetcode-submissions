class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        prefix[0] = 1
        suffix[len(nums) - 1] = 1 
        for i in range(1, len(nums)):
            i2 = len(nums) - 1 - i
            prefix[i] = nums[i - 1] * prefix[i - 1]
            suffix[i2] = nums[i2 + 1] * suffix[i2 + 1]
        
        for i in range(len(nums)):
            nums[i] = prefix[i] * suffix[i]
        
        return nums