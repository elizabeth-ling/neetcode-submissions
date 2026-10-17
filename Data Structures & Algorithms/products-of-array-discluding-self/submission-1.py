class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        suffix = [1 for _ in range(len(nums))]

        product = 1
        for n in nums: 
            prefix.append(product)
            product *= n
        
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = product
            product *= nums[i]
        
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])

        return res