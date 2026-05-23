class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # initialize the bottom row and left most column to be 1
        # everytile is the sum of dp of the right and bottom do a bottom up approach

        row = [1] * m 
        dp = ([[1] * n]) * m

        for i in range(m - 2, -1, -1):

            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        
        return dp[0][0]

