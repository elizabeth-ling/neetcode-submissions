"""
loop through s
if c is a closed bracket, stack.pop() should be the matching bracket
if c is an open bracket, add to stack 

if stack is empty, return True
else False
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeMapOpen = { ")" : "(",
                         "]" : "[",
                         "}" : "{"}
        
        for c in s:
            if c in closeMapOpen:
                if not stack or stack.pop() != closeMapOpen[c]:
                    return False
            else:
                stack.append(c)

        if stack:
            return False
        
        return True
