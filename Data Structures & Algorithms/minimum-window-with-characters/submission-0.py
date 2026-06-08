"""
sliding window 
- l, r = 0, len(t) - 1 (must be at minimum this big)
- build hashmap of chars in t and freq
- keep hashmap of chars in window and freq
- update res if ??? and if cur_len < len(res)
    - option 1: traverse keys of t hashmap, check if freq matches 
    - option 2 (faster): keep track of satisfied matches and unsatisfied
- expand window if ()
    - each r += 1, update map[r] += 1
- shrink window if ()
    - each l += 1, update map[l] -= 1

"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freq_t = defaultdict(int)
        freq_w = defaultdict(int)

        # build hashmap for char, freq in t
        for c in t:
            freq_t[c] += 1

        res_len = float('inf')
        res = ""
        have, need = 0, len(freq_t)
        l = 0

        for r, c in enumerate(s):
            freq_w[c] += 1

            if c in freq_t and freq_w[c] == freq_t[c]:
                have += 1
            
            while have == need:
                cur_len = r - l + 1
                
                if cur_len < res_len:
                    res_len = cur_len
                    res = s[l:r + 1]
                
                freq_w[s[l]] -= 1

                if s[l] in freq_t and freq_w[s[l]] < freq_t[s[l]]:
                    have -= 1
                
                l += 1

        return res

    
        

        