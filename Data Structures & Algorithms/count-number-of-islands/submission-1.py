class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # visited = [[False] * (len(grid[0])) for _ in range(len(grid))]
        res = 0

        rows = len(grid[0])
        cols = len(grid)

        def dfs(r, c):
            # 1) bounds check
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            # 2) water or already visited
            if grid[c][r] == '0': #or visited[r][c]:
                return

            # visited[r][c] = True
            grid[c][r] = '0'

            # 3) recurse in four directions
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[c][r] == '1':
                # if grid[r][c] == '1' and not visited[r][c]:
                    dfs(r, c)
                    res += 1

        return res
