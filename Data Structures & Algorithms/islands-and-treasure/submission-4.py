class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        dist = 0
        visited = set()
        # setup - marking all bfs starting position
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r, c))

        def bfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == -1 or (r, c) in visited:
                return
            visited.add((r, c))
            q.append([r, c])
        
        # solve with bfs
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                bfs(r - 1, c)
                bfs(r + 1, c)
                bfs(r, c - 1)
                bfs(r, c + 1)
            dist += 1
