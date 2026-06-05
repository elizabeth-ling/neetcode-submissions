"""
two pointers
- since we don't need indices, we can sort nums
1. sort nums 
2. loop through nums using i until nums[i] is a negative number
3. use two pointers to search remaining numbers until 
   nums[l] + nums[r] == -1 * nums[i]
* l = 0, r = len(nums) - 1
* diff = -1 * (nums[l] + nums[r])
* check if diff is in nums


nums = [-1,0,1,2,-1,-4]
nums = [-4, -1, -1, 0, 1, 2]
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i, cur in enumerate(nums):
            # no need to go through remaining because they're positive
            if cur > 0:
                break
            
            # handling duplicates
            if i > 0 and cur == nums[i - 1]:
                continue
            
            # initialize two pointers to go through remaining nums
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[l] + nums[r] + cur

                if total == 0:
                    res.append([cur, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip duplicated
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                elif total > 0:
                    r -= 1
                else:
                    l += 1

        return res

