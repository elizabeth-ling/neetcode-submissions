"""
similar to optimal solution of two anagrams problem 

- initialize a freq array ([0] * 26) for each word in strs. order of the character corresponds to the index value
- convert to a tuple, since hashmaps can't have an array as the key 
- the value of the tuple stores the actual word 
- return the values of the hashmap as an array 
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs: 
            freq = [0] * 26

            for c in s: 
                freq[ord(c) - ord('a')] += 1
            
            res[tuple(freq)].append(s)
        
        return list(res.values())


