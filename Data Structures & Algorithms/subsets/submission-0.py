class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums_length = len(nums)

        def backtrack(index, path):
            # Base case
            if index == nums_length:
                res.append(path[:])
                return

            # Decision 1: include nums[index]
            path.append(nums[index])
            backtrack(index + 1, path)

            # Decision 2: skip nums[index]
            path.pop()
            backtrack(index + 1, path)

        backtrack(0, [])
        return res