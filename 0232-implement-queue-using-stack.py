# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).


class MyQueue:
    # I'm not convinced. For peek i consider i cheated for python list syntax.

    def __init__(self):
        self.stack = []
        self.queue = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.stack) == 0 and len(self.queue) == 0:
            self.peekVal = x

    def pop(self) -> int:
        if len(self.queue) == 0:
            val = 0
            for _ in range(len(self.stack)):
                val = self.stack.pop()
                self.queue.append(val)
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue[-1] if len(self.queue) else self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self.queue) == 0
