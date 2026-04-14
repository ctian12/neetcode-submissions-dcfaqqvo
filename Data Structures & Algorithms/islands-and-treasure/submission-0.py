from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        chests = deque()

        def expand(r, c):
            neighbors = []
            if r > 0 and grid[r - 1][c] > grid[r][c] + 1:
                grid[r - 1][c] = grid[r][c] + 1
                neighbors.append((r - 1, c))
            if r < rows - 1 and grid[r + 1][c] > grid[r][c] + 1:
                grid[r + 1][c] = grid[r][c] + 1
                neighbors.append((r + 1, c))
            if c > 0 and grid[r][c - 1] > grid[r][c] + 1:
                grid[r][c - 1] = grid[r][c] + 1
                neighbors.append((r, c - 1))
            if c < cols - 1 and grid[r][c + 1] > grid[r][c] + 1:
                grid[r][c + 1] = grid[r][c] + 1
                neighbors.append((r, c + 1))
            return neighbors

        # Add all chests (0s) as starting points
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    chests.append((r, c))
        
        # BFS loop
        while chests:
            r, c = chests.popleft()
            for nr, nc in expand(r, c):
                chests.append((nr, nc))
