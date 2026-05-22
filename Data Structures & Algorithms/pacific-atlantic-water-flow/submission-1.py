class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        row = len(heights)
        col = len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visit, prevH):
            if c < 0 or c >= col or r < 0 or r >= row or heights[r][c] < prevH or (r, c) in visit:
                return 
            
            #case 
            visit.add((r, c))
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])

        for c in range(col):
            # first row on pac 
            dfs(0, c, pac, 0)
            # last row on atl
            dfs(row - 1, c, atl, 0)

        for r in range(row):
            # first col on pac
            dfs(r, 0, pac, 0)
            # last col on atl
            dfs(r, col - 1, atl, 0)

        for r in range(row):
            for c in range(col):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
            
            



