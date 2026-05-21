class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maximum = 0
        l , r = 0 , len(heights)-1
        while l<r:
            # we are finding area so min of 2 heights times width between indicies
            current = ( (min(heights[l], heights[r])) * (r - l) )

            #we check and move the smaller heights because larger height = more capacity
            if heights[l] < heights[r]:
                l +=1
            elif heights[l] >  heights[r]: 
                r -=1
                # crucial to handle same heights edge case,  can move either pointer here
            elif heights[l] ==  heights[r]:
                l+=1
            #set max value if current is larger 
            maximum = max(maximum, current)
        return maximum

        