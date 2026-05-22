class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        k = 0
        for i in range(len(prices)):
            # buy 
            if prices[i] < prices[k]:
                k = i

            # sell
            if prices[i] - prices[k] > profit:
                profit = prices[i] - prices[k]
                print(profit)

        return profit

            
