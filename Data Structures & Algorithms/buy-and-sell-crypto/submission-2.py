class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force Solution 
        profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices),1):
                
                profit = max(prices[j]-prices[i] , profit)
        return profit
