class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict()
        ans = []

        for s in strs: 
            st = tuple(sorted(s))

            if st in res: 
                res[st].append(s)
            else:
                res[st] = [s]
        
        for key in res:
            ans.append(res[key])

        return ans
            

"""
sort each string, group using hash map
O(m * n logn)
"""