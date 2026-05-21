class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maximum = 0
        l , r = 0 , len(heights)-1
        while l<r:
            current = ( (min(heights[l], heights[r])) * (r - l) )
            if heights[l] < heights[r]:
                l +=1
            elif heights[l] >  heights[r]: 
                r -=1
            elif heights[l] ==  heights[r]:
                l+=1
            maximum = max(maximum, current)
        return maximum

        