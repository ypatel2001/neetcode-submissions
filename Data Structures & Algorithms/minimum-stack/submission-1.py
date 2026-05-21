class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

# we init and maintain a minstack that helps us keep track of the min value at any given
#index in the main stack, sort of a running track, we add and pop from it whenever we add/pop
# from the main stack 
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min (val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

        
