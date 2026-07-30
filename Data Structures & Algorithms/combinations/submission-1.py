"""
solution is found when length of path array == k

at each step, you can choose between any of the numbers in the range [1, n],
not including the numbers before
- we handle this by keeping track of the current index, (cur)
- the choices are between [cur, n] range(cur, n+1)
- append choice in range(cur, n+1) to path, continue, then backtrack 

"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(cur, path):
            if len(path) == k:
                res.append(path[:])
                return
            
            for num in range(cur, n+1):
                path.append(num)
                backtrack(num+1, path)
                path.pop()

        backtrack(1, [])
        return res
