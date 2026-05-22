class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        res = 0
        dp = {}
        def dfs(r, c):
            # invalid
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]

            if r == m - 1 and c == n - 1:
                return 1
            res = dfs(r + 1, c) + dfs(r, c + 1)

            dp[(r, c)] = res

            return res
        
        return dfs(0,0)
