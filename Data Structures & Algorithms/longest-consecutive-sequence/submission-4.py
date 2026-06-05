
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        maxx = 0

        for num in nums:
            if not hashmap[num]:
                # update count of newly added number 
                hashmap[num] = hashmap[num - 1] + hashmap[num + 1] + 1

                # update count of number at start of consec. sequence
                hashmap[num - hashmap[num - 1]] = hashmap[num]

                # update count of number at end of consec. sequence
                hashmap[num + hashmap[num + 1]] = hashmap[num]
                
                # update maxx
                maxx = max(maxx, hashmap[num])
        
        return maxx