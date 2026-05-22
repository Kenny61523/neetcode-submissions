class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #edge case 
        rows = len(board)
        cols = len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        # cannot modify tne board
        def dfs(r, c, i):
            # case invalid
            if (r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] == True 
                or board[r][c] != word[i] or i >= len(word)):
                return False

            if i == len(word) - 1:
                return True 
            # case valid
            visited[r][c] = True
            
            res = (dfs(r - 1, c, i + 1) or 
            dfs(r + 1, c, i + 1) or 
            dfs(r, c - 1, i + 1) or
            dfs(r, c + 1, i + 1))

            # backtrack
            visited[r][c] = False

            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False
    