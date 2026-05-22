class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # create the dp mapping of amount to number of coins needed
        dp = [amount + 1] * (amount + 1)
        # base case
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c < 0: 
                    break
                dp[i] = min(dp[i], dp[i - c] + 1)
                print(i, dp[i])
        
        return dp[amount] if dp[amount] != amount + 1 else -1