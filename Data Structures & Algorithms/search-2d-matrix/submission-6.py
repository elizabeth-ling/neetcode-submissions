"""
INTUITION:
- sorted => binary search
- set l and r pointers
    - l, r = 0, ROWS * COLS - 1
- calculate middle index
    - m = l + ((r - l) // 2)


l = 0 
r = 4
m = 2
row = 2 /% 4 = 0
col = 2 // 3 = 0

matrix[row][col] = 11
since 11 > 10, 
r = 4
"""

# Time: O(log(m * n))
# Space: 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1

        while l <= r:
            m = l + ((r - l) // 2)
            row, col = m // COLS, m % COLS

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m + 1
            else:
                r = m - 1

        return False








