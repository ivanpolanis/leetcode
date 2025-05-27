class Solution:
    def recursive(self, stack, string,open,close,n):
        if len(string) == 2 * n:
            return stack.append(string)
        if open < n:
            self.recursive(stack,string + '(',open + 1, close,n)
        if open > close:
            self.recursive(stack,string + ')',open,close + 1, n)

    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        self.recursive(stack,"",0,0,n)
        return stack

