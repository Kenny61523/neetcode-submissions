from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        row, col = len(grid), len(grid[0])
        q = deque()
        fresh_b = 0
        # traverse through grid and mark all starting points (rotented banana)
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    fresh_b += 1
        
        if fresh_b == 0:
            return res

        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        # mark adjacent banana cells as rottene each time increasing res
        while q and fresh_b > 0:
            qLen = len(q)
            res += 1
            for i in range(qLen):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr >= row or nc < 0 or nc >= col or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append([nr,nc])
                    fresh_b -= 1
        print(fresh_b)
        return res if fresh_b == 0 else -1
