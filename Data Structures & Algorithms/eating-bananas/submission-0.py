class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # by setting r to max in piles , effectively gives us a range from 1 to max value
        l , r = 1 , max(piles) 
        res = r #max possible solution 

        while l <=r:
            k = (l+r) // 2
            hours = 0 
            for p in piles:
               hours+=math.ceil( p / k ) 
            if hours <=h:
                res= min(res, k )
                r = k -1 #search left portion 
            else:
                l = k + 1 #search right portion
        return res