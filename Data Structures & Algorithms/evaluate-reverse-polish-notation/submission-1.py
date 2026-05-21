class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a , b = stack.pop() , stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a , b = stack.pop() , stack.pop()
                #doing int() here fulfills condition of needing division
                #to round to 0 instead of rounding down like it does in python
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[-1] #can also do stack[0]
