class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9): 
                val = board[row][col]

                if val == '.':
                    continue
                
                box = (row // 3, col // 3)
                if val in rows[row] or val in cols[col] or val in boxes[box]:
                    return False
                
                rows[row].add(val)
                cols[col].add(val)
                boxes[box].add(val)
        
        return True


