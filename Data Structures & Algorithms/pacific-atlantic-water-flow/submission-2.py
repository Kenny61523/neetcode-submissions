class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        atl, pac = set(), set()

        def dfs(r, c, visit, prevH):
            if ((r, c) in visit or r < 0 or r == row or c < 0 or c == col or heights[r][c] < prevH):
                return
            
            visit.add((r, c))
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
        
        #checkign top and bottom
        for r in range(row):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, col - 1, atl, heights[r][col - 1])

        for c in range(col):
            dfs(0, c, pac, heights[0][c])
            dfs(row - 1, c, atl, heights[row - 1][c])
        
        res = []
        for r in range(row):
            for c in range(col):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])

        return res

    

