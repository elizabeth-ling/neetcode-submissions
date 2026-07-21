"""
nums = [1, 2, 3]



"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path):
            # Base case: if len(path) == len(nums)
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for num in nums:
                # constraint: no repeats
                if num in path:
                    continue 

                path.append(num)
                backtrack(path)
                path.pop() # backtrack 

        backtrack([])
        return res
