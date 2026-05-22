class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        row = len(grid)
        col = len(grid[0])

        def dfs(r, c):
            #out of bounds
            if r < 0 or c < 0 or r >= row or c >= col:
                return
            
            if grid[r][c] == '0':
                return

            grid[r][c] = '0'

            dfs(r + 1, c)
            dfs(r , c + 1)
            dfs(r, c - 1)
            dfs(r - 1, c)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r, c)

        return res