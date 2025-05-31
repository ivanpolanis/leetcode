# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).


class MyStack:

    def __init__(self):
        self.queue = []
        self.topVal = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.topVal = x

    def pop(self) -> int:
        temp = []
        l = len(self.queue) - 1
        i = 0
        while i < l:
            val = self.queue.pop(0)
            if i == l - 1:
                self.topVal = val
            temp.append(val)
            i += 1

        val = self.queue.pop(0)
        self.queue = temp
        return val

    def top(self) -> int:
        return self.topVal

    def empty(self) -> bool:
        return len(self.queue) == 0
