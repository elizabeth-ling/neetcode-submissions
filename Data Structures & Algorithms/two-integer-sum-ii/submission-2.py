class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = dict()

        for i, num in enumerate(numbers):
            need = target - num

            if need in seen: 
                return [seen[need], i + 1]
            
            seen[num] = i + 1
        