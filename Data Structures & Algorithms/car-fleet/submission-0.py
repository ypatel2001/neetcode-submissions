class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #merges the pairs of position and speed  into one array of pairs
        pair = [(p , s) for (p,s) in zip(position, speed)]
        pair.sort()

        stack = []

        for p,s in pair[::-1]: 
            #getting the time it takes that car to reach target
            #adding to the stack
            stack.append((target - p ) /s) 
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

