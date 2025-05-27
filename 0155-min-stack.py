# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class MinStack:

    def __init__(self):
        self.pref = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.pref) == 0 or val < self.pref[len(self.pref)-1]:
            self.pref.append(val)
        else:
            self.pref.append(self.pref[len(self.pref)-1])
        

    def pop(self) -> None:
        self.stack.pop()
        self.pref.pop()
        

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]
        

    def getMin(self) -> int:
        return self.pref[len(self.pref) - 1]
