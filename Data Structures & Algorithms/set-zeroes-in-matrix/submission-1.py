from collections import deque

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        # bfs on the matrix without allocating another matrix
        ROWS = len(matrix)
        COLS = len(matrix[0])

        q = deque()
        # mark
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    q.append((r, c))
        print(q)

        # helper        
        def dfs(row, col):
            for i in range(COLS):
                matrix[row][i] = 0
            for j in range(ROWS):
                matrix[j][col] = 0
            return
        
        # call dfs
        while q:
            (row, col) = q.popleft()
            dfs(row, col)

        