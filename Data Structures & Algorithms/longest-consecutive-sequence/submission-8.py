
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}
        res = 0

        for n in nums: 
            if n not in mp:
                l = mp.get(n - 1, 0)
                r = mp.get(n + 1, 0)
                length = l + r + 1

                mp[n] = length
                mp[n - l] = length
                mp[n + r] = length

                res = max(res, length)

        return res

        