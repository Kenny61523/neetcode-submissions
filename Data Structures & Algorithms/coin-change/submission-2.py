class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # position in the array stores the number of coins needed to form the value
        numCoins = [amount + 1] * (amount + 1)
        numCoins[0] = 0 # base case

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    numCoins[a] = min(numCoins[a], numCoins[a - c] + 1)
        
        return numCoins[amount] if numCoins[amount] != amount + 1 else -1