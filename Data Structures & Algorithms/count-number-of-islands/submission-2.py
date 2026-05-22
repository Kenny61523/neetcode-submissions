class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        
        def dfs(r, c):
            #out of bounds return 
            if r < 0 or c < 0 or r >= row or c >= col:
                return
            
            #skip if if element is '0'
            if grid[r][c] == '0':
                return
            
            #otherwise turn 1 -> 0
            grid[r][c] = '0'

            #recursive call to dfs to 4 directions
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r, c)
                    print("aa")
            print("bb")
        
        return res

