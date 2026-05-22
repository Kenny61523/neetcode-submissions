import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }

        stack = []
        
        for i in range(len(tokens)):
            if tokens[i] in op:
                a = stack.pop()
                b = stack.pop()

                result = op[tokens[i]](int(b), int(a))
                stack.append(int(result))
            else:
                stack.append(tokens[i])

        return int(stack[-1])
