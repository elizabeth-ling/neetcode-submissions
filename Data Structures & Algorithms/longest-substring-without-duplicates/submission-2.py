"""
sliding window
- l
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, max_len = 0, 0, 0
        
        while (l <= r and r < len(s)):
            if s[r] in s[l:r]:
                if r - l > max_len:
                    max_len = r - l
                l += 1
            else:
                r += 1

        if r - l > max_len:
            max_len = r - l
            l += 1
        return max_len