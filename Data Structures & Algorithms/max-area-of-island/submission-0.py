class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        maxIsland = 0
        numIsland = 0

        def dfs(r, c):
            # return on out of bounds
            if r < 0 or c < 0 or r >= row or c >= col:
                print("aa")
                return 0 
            
            # reutrn if water
            if grid[r][c] == 0:
                print("bb")
                return 0

            grid[r][c] = 0
            print('aaa')

            # return 1

            # dfs(r + 1, c)
            # dfs(r, c + 1)
            # dfs(r, c - 1)
            # dfs(r - 1, c)
            return(dfs(r + 1, c) + dfs(r, c + 1) + dfs(r, c - 1) + dfs(r - 1, c) + 1)

            
            # grid[r][c] = '0'
            # print('aaa')
            # return 1
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    # numIsland = 0
                    maxIsland = max(maxIsland, dfs(r, c))
        
        return maxIsland

            
            