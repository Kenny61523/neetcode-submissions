class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        def dfs(i, j, index):
            if index == len(word): return True # word found

            if ((i >= len(board) or i < 0 ) or 
               ( j >= len(board[0]) or j < 0) or 
                (i, j) in path):
                return False
            if (board[i][j] != word[index]): return False

            path.add((i, j))
            res = (dfs(i - 1, j, index + 1) or
                    dfs(i + 1, j,  index + 1) or
                    dfs(i, j - 1,  index + 1) or
                    dfs(i, j + 1,  index + 1))
            path.remove((i, j))
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]: # find the first word 
                    if dfs(i, j, 0): return True
        
        return False
