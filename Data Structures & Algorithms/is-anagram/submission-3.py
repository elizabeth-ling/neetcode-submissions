# O(n + m) solution 
"""
O(n + m)
create arrays of s and t counting the occurences of letters. the index value corresponds to the order of the character

if the arrays are the same, they are anagrams
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = [0] * 26
        count_t = [0] * 26

        for c in s:
            count_s[ord(c) - ord('a')] += 1
        
        for c in t: 
            count_t[ord(c) - ord('a')] += 1
        
        return count_s == count_t