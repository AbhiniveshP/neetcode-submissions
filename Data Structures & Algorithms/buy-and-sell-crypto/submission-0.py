class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (prices is None or len(prices) < 2):
            return 0
        
        minSoFar, maxProfit = prices[0], 0
        
        for i in range(len(prices)):
            price = prices[i]
            profit = max(0, price - minSoFar)
            maxProfit = max(profit, maxProfit)
            minSoFar = min(price, minSoFar)
        
        return maxProfit