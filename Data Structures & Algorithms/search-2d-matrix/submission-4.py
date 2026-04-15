class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = (len(matrix) * len(matrix[0]))
        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2
            x = m // len(matrix[0])
            y = m % len(matrix[0])
            val = matrix[x][y]

            if val == target:
                return True
            elif val > target:
                r = m - 1
            else:
                l = m + 1
        
        return False