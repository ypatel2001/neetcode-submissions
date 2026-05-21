class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # init left and right at start, maxP at 0 default case
        # l = 0 
        # r =  1 
        # maxP = 0 

        # while r < len(prices):
        #     # is the trade profitable at current pointers/window
        #     if prices[l] < prices[r]:
        #         #take max of curr maxP and current trade profit
        #         currentprofit = prices[r]- prices[l]
        #         maxP = max(maxP, currentprofit )
        #     # if trade not profitable we slide window ahead
        #     # to find next lower buy in (left pointer)
        #     else: 
        #         l = r
        #     # the base case is once we have slide the window ahead w/ l=r
        #     # we want to increment the right pointer by 1 to view next day 
        #     #and check for profitability again (repeat)
        #     r +=1
        # return maxP


        l = 0 
        r = 1 
        maxP = 0 

        while r < len(prices):
            if prices[l] < prices[r]:
                currentProfit = prices[r] - prices[l]
                maxP = max(maxP , currentProfit)
            else: 
                l = r 
            r +=1 
        return maxP