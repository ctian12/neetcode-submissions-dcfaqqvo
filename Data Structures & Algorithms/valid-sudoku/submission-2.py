class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                row = i
                col = j
                box = (i // 3) * 3 + (j // 3)

                if val == ".":
                    continue

                rowKey = (row, val, "row")
                colKey = (col, val, "col")
                boxKey = (box, val, "box")

                if rowKey in seen or colKey in seen or boxKey in seen:
                    return False
                
                seen.add(rowKey)
                seen.add(colKey)
                seen.add(boxKey)
        
        return True
