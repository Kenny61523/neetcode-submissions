class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = set()
        dist = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        def update(r, c):
            # invalid 
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == -1 or (r, c) in visited:
                return 
            q.append((r, c))
            visited.add((r, c))

        # udapte grid step by step 
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                print(r, c)
                grid[r][c] = dist
                update(r - 1, c)
                update(r + 1, c)
                update(r, c - 1)
                update(r, c + 1)
            dist += 1
        
        return


