class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        row = len(grid)
        col = len(grid[0])
        q = deque()
        visited = set()

        # set up for bfs by marking all grid with 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        def addGrid(r, c):
            if (r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == -1 or
             (r, c) in visited):
                return 
            visited.add((r, c))
            q.append([r, c])

        dist = 0
        while q:
            for i in range(len(q)):
                (r, c) = q.popleft()
                grid[r][c] = dist
                addGrid(r - 1, c)
                addGrid(r, c - 1)
                addGrid(r + 1, c)
                addGrid(r, c + 1)
            dist += 1        
        # return grid

      