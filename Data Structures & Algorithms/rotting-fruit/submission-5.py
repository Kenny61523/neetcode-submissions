class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs from rotten fruit
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = set()
        res = 0

        # set up 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))

        # 
        def bfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid[r][c] != 1:
                return 
            grid[r][c] = 2
            q.append((r, c))
            visited.add((r, c))

        while q:
            for n in range(len(q)):
                r, c = q.popleft()
                bfs(r - 1, c)
                bfs(r + 1, c)
                bfs(r, c - 1)
                bfs(r, c + 1)
            res += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return res - 1 if res > 0 else 0