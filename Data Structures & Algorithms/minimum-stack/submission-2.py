class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1: 
            self.minstack.append(val)
        else:
            prev = self.minstack.pop()
            self.minstack.append(prev)
            self.minstack.append(min(val, prev))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        
    def top(self) -> int:
        if self.stack is None: 
            return None
        
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
