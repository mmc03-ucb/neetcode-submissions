from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minVal = deque()

    def push(self, val: int) -> None:
        # Always push the value onto the stack
        self.stack.append(val)
        
        # If the min stack is empty or the new value is less than or equal to the current min, push it onto the min stack
        if not self.minVal or val <= self.minVal[-1]:
            self.minVal.append(val)

    def pop(self) -> None:
        # Only pop from the min stack if the top of the min stack is the same as the top of the main stack
        if self.stack[-1] == self.minVal[-1]:
            self.minVal.pop()  # Remove the top from min stack
        self.stack.pop()  # Remove the top from the main stack

    def top(self) -> int:
        # Return the top of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top of the min stack (which always holds the current minimum)
        return self.minVal[-1]
