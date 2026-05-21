class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
    # Initialize the output list with 0s. The length is the same as the input temperatures.
        # 0 is the default value, meaning no warmer future day found (yet).
        output = [0] * len(temperatures)
        
        # Initialize a stack. This stack will store tuples of (temperature, index).
        # It will maintain a monotonically decreasing order of temperatures.
        # Meaning: stack[-1] (top) will be <= stack[-2] <= stack[-3] ... 
        stack = [] 

        # Iterate through the temperatures list, getting both the index 'i' and the temperature 't'.
        for i, t in enumerate(temperatures):
            
            # While the stack is not empty AND the current temperature 't' is greater than 
            # the temperature at the top of the stack (stack[-1][0]).
            while stack and t > stack[-1][0]:
                # If the current temperature 't' is warmer than the day at the top of the stack:
                # Pop the stack element (which contains the temperature and index of that past day).
                stackT, stackInd = stack.pop() 
                
                # Calculate the number of days waited: current index 'i' - past day's index 'stackInd'.
                # Store this difference in the output list at the index of the past day.
                output[stackInd] = i - stackInd
                
            # After the while loop, either the stack is empty or the current temperature 't'
            # is less than or equal to the temperature at the top of the stack.
            # Append the current temperature and its index onto the stack. 
            # This maintains the monotonically decreasing property.
            stack.append((t, i))
            
        # After iterating through all temperatures, any indices remaining on the stack 
        # never found a warmer day, so their output values remain 0.
        # Return the completed output list.
        return output