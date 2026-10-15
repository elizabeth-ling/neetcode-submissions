class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs: 
            st = tuple(sorted(s))
            res[st].append(s)
        
        return list(res.values())