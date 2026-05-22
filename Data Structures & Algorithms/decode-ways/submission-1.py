class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1} # if it reaches the end thats one valid combination
        res = 0
        # '1090'
        def dfs(i):
            # case reaches to the end return 1
            if i in dp:
                return dp[i]
            # case 0 appears in the beginning return 0 invalid. 
            if (s[i] == '0'):
                return 0

            res = dfs(i + 1)

            if (i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7'))):
                res += dfs(i + 2)

            dp[i] = res
            return res

        return dfs(0)
