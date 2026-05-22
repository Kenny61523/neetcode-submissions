from typing import List
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
                # s
                # tokens[i] = int(tokens[i - 1]) op[tokens[i]] int(tokens[i - 2])
                #  if token in op:  # Check if the token is an operator
                # Pop the last two numbers from the stack
                b = stack.pop()
                a = stack.pop()
                # Perform the operation and push the result back onto the stack
                stack.append(op[tokens[i]](int(a), int(b)))
            else:
                stack.append(tokens[i])
            
        return int(stack[-1])
