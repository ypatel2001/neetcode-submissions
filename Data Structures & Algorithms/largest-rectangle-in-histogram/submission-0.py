class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            # while stack top height is greater than current height we pop
            # as the new height is bounding the area
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # we do the area as current index i - stored index
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        # go thru remainng stack to check if stacks remaining are 
        # eligible for the max height 
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea