"""
strs = ["xx",
        "xxxxxxx",
        ""]

encode(strs) = "3.2#xx7#xxxxxxx0#"
decode(encode(strs)) = ["xx",
                        "xxxxxxx",
                        ""]

strs = []
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s))
            res += '#'
            res += s
        
        return res

    # encode(strs) = "2#xx7#xxxxxxx0#"
    def decode(self, s: str) -> List[str]:
        res = []
        lengthS = ""
        i = 0

        while i < len(s):
            if s[i] == '#':
                j = int(lengthS)
                res.append(s[i+1:i+1+j])
                i += j + 1
                lengthS = ""
            else:
                lengthS += s[i]
                i += 1
        
        return res
