class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        res = []

        for n in nums:
            freq[n] += 1
        
        # index corresponds to frequency 
        bucket = [[] for _ in range(len(nums) + 1)]

        for n in freq:
            bucket[freq[n]].append(n)
        
        
        while k:
            if bucket[-1] == []:
                bucket.pop()
            else:
                res.append(bucket[-1].pop())
                k -= 1

        return res
