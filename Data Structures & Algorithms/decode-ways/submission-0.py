class Solution:
    def numDecodings(self, s: str) -> int:
        # "123202" -> 1,2,3,20,2 or 12,3,20,2 or 1,23,20,2 
        # special case for 1 and 2
        # when 0 -> check if the prev char is 1 or 2 else invalid
        dp = { len(s): 1} # string is complete if it reaches the end
        
        def dfs(i):
            if i in dp: # array reaches end -> valid combination
                return dp[i]
            if s[i] == "0": # 0 appears somewherein the middle -> invalid
                return 0
            
            res = dfs(i + 1) #
            if (i + 1 < len(s) and 
                (s[i] == "1" or (s[i] == "2" and s[i + 1] < '7'))):
                res += dfs(i + 2) #

            dp[i] = res 
            return res

        return dfs(0)