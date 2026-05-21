class Solution:
    def trap(self, height: List[int]) -> int:
        # return 0 if height is not defined
        if not height:
            return 0 
        #start pointers and output var
        l = 0 
        r = len(height) - 1 

        output = 0 
        leftMax, rightMax = height[l], height[r]
        while l < r :
            #if leftMax height is less than rightMax
            if leftMax < rightMax:
               # we increment the smaller pointer , left here
                l += 1
                #update leftMax  to max of leftMax and current h[L]
                leftMax = max(leftMax, height[l])
                #add to the output leftMax - current height at L
                output += leftMax - height[l]
            else:
                 # we increment the smaller pointer , right here
                r -=1 
                #update rightMax  to max of rightMax and current h[R]
                rightMax = max(rightMax , height[r]) 
                #add to the output rightMax - current height at R
                output += rightMax - height[r]
        return output