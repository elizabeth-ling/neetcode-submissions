"""
2D binary search 

"""

class Solution:
    def binarySearchArray(self, l: int, r: int, arr: List[int], target) -> bool:
        if l > r:
            return False
        
        idx = l + (r - l) // 2

        if arr[idx] == target:
            return True
        if arr[idx] > target:
            return self.binarySearchArray(l, idx - 1, arr, target)
        return self.binarySearchArray(idx + 1, r, arr, target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0]) - 1
        for i in range(0, len(matrix)):
            if matrix[i][n] >= target:
                return self.binarySearchArray(0, n, matrix[i], target)
        
        return False

        