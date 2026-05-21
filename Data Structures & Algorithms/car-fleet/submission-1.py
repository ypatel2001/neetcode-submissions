class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #merges the pairs of position and speed  into one array of pairs
        pair = [(p , s) for (p,s) in zip(position, speed)]
        pair.sort()
        #holds the computed arrival times  so we can directly compare them
        stack = []

        for p,s in pair[::-1]: 
            #getting the time it takes that car to reach target
            #adding to the stack
            stack.append((target - p ) /s) 
        #checks for min 2 items in stack and top is less than second to top 
        #we want to check that the time we just added is less than the preceeding
        #if it is then we pop it immediately bc it means the car caught up and now
        #its speed is dictated by the slower speed at -2
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

