class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minVal = prices[0]
        for p in prices:
            minVal = min(minVal, p)
            profit = p - minVal
            if minVal < p and maxProfit < profit:
                maxProfit = profit
    
        return maxProfit