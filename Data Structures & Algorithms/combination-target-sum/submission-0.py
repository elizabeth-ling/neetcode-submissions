"""
- if we include, index stays, since we can reuse numbers
- if we skip, index moves

- result is found when sum of path == target, so keep a running sum of your path
- dead end is found if sum of path > target, or if path length is greater than nums length


"""

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, path, total):
            # Base case: result found, sum of path == target
            if total == target:   
                res.append(path[:])
                return 
            
            # Dead ends
            if total > target or i >= len(nums):
                return 

            for num in nums[i:]:
                path.append(num)
                backtrack(i, path, total+num)
                path.pop()
                i += 1
                

        backtrack(0, [], 0)
        return res