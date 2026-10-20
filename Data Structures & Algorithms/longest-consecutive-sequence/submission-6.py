
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0

        for num in nums_set:
            # if num - 1 is not in the set, then num is the start of a sequence
            if num - 1 not in nums_set: 
                cur_length = 1
                while num + cur_length in nums_set:
                    cur_length += 1

                max_length = max(max_length, cur_length)
        
        return max_length

        