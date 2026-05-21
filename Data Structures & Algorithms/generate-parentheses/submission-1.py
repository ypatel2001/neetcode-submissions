class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # List to store the final valid parenthesis combinations.
        output = [] 
        # List used as a character stack to build the current parenthesis string.
        stack = []  

        # Define the recursive backtracking function.
        # openN: count of '(' parentheses currently in the stack.
        # closedN: count of ')' parentheses currently in the stack.
        def backtrack(openN, closedN):
            
            # Base Case: If the number of open and closed parentheses both equal n,
            # we have formed a complete and valid combination.
            if openN == closedN == n:
                # Join the characters in the stack to form the string and add it to the output list.
                output.append("".join(stack))
                # Return to explore other possibilities.
                return 

            # Recursive Step 1: Try adding an open parenthesis '('
            # Condition: We can add '(' only if we haven't used up all 'n' available open parentheses.
            if openN < n:
                # Add '(' to the current path (stack).
                stack.append('(')
                # Recurse with an incremented open count.
                backtrack(openN + 1, closedN)
                # Backtrack: Remove the '(' we just added to explore other possibilities.
                stack.pop() 

            # Recursive Step 2: Try adding a closed parenthesis ')'
            # Condition: We can add ')' only if the number of closed parentheses 
            # is less than the number of open parentheses already added. 
            # This ensures the parentheses remain well-formed at each step.
            if closedN < openN:
                # Add ')' to the current path (stack).
                stack.append(')')
                # Recurse with an incremented closed count.
                backtrack(openN, closedN + 1)
                # Backtrack: Remove the ')' we just added.
                stack.pop()
        
        # Start the backtracking process with 0 open and 0 closed parentheses used.
        backtrack(0, 0)
        # Return the list containing all generated valid combinations.
        return output