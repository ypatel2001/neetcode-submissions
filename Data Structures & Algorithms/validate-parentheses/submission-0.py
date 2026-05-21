class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to keep track of opening brackets
        stack = []
        # Dictionary to map closing brackets to their corresponding opening brackets
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        # Iterate over each character in the input string
        for c in s:
            # If the character is a closing bracket
            if c in closeToOpen:
                # Check if the stack is not empty and the top of the stack is the matching opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    # If so, pop the top of the stack
                    stack.pop()
                else:
                    # If not, the string is not valid
                    return False
            else:
                # If the character is an opening bracket, push it onto the stack
                stack.append(c)
        
        # If the stack is empty, all opening brackets have been matched, so the string is valid
        return True if not stack else False