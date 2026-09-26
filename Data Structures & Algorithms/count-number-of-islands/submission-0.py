class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()
        islands = 0

        def valid(row, col):
            return 0 <= row < rows and 0 <= col < cols and grid[row][col] == '1'

        def dfs(row, col):
            for dx, dy in directions:
                next_r, next_c = row + dy, col + dx
                if valid(next_r, next_c) and (next_r, next_c) not in seen:
                    seen.add((next_r, next_c))
                    dfs(next_r, next_c)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in seen:
                    seen.add((i, j))
                    islands += 1
                    dfs(i, j)
        
        return islands
