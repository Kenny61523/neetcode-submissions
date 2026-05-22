class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        # mark for both pac and atl -> check if a position is in both sets add to res
        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight):
            if (r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or 
                prevHeight > heights[r][c]):
                return 
            
            # mark visited
            visited.add((r, c))
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        # bfs from the borders
        for r in range(rows):
            dfs(r, cols - 1, atl, heights[r][cols - 1])
            dfs(r, 0, pac, heights[r][0])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r,c])
        return res



