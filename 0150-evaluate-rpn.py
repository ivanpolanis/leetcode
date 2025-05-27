class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case '+':
                    first, second= stack.pop(), stack.pop()
                    stack.append(second + first)
                case '/':
                    first, second= stack.pop(), stack.pop()
                    stack.append(int(second / first))
                case '-':
                    first, second= stack.pop(), stack.pop()
                    stack.append(second - first)
                case '*':
                    first, second= stack.pop(), stack.pop()
                    stack.append(second * first)
                case _:
                    stack.append(int(token))
        return stack.pop()
