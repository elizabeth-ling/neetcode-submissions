class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        res = ""
        for s in strs:
            res += str(len(s))
            res += '#'
            res += s
        
        return res
        

    def decode(self, s: str) -> List[str]:
        if not s: 
            return []
        
        res, i = [], 0
        while i < len(s):
            num = ""
            j = i
            while s[j] != '#':
                num += s[j]
                j += 1
            num = int(num)
            res.append(s[j + 1:j + num + 1])
            i, j = j + 1 + num, j + num
        return res

