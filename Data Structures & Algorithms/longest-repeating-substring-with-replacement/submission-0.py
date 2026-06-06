"""
sliding window 
- in any given substring, the optimal # of replacements is going to be 
  len(substring) - numHighFreqChar
    - i.e in "AAABA" the optimal # of replacements is going to be 5 - 4 = 1,
      since 'A' is the highest freq character
    - keep track of highest freq character in your window
    - keep moving r pointer until number of the non-high freq characters
      is greater than your max number of replacements (k)
      - while window_lenth - highest_freq > k:
            shrink left

- how to keep track of characters + freq?
    - since s consists only of uppercase chars, can use this:
    - freq = [0]*26, where the index matches the letter. 
      freq[0] = frequency of the letter A in that substring?
    - must also keep track of max_freq of freq
    - each time you read a new character, if freq[char] > max_freq, update
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, max_len, max_freq = 0, 0, 0
        freq = [0] * 26

        for r in range(len(s)):
            freq[ord(s[r]) - ord('A')] += 1

            max_freq = max(max_freq, freq[ord(s[r]) - ord('A')])

            cur_len = r - l + 1

            while cur_len - max_freq > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
                cur_len = r - l + 1
            
            max_len = max(max_len, cur_len)
        
        return max_len

        