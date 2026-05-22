class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        COL = len(grid[0])
        ROW = len(grid)
        res = 0
        # do a dfs serach to paint all the tiles of the island to "0"
        def dfs(r, c):
            if c < 0 or c >= COL or r < 0 or r >= ROW or grid[r][c] == "0":
                return 
            grid[r][c] = "0"
            
            dfs(r, c - 1)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r + 1, c)
            return 

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res