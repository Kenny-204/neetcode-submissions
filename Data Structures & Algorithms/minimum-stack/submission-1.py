class MinStack:

    def __init__(self):
        self.stack = []
        return

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append([val,val])
        else: self.stack.append([min(self.stack[-1][0],val),val])
        return

    def pop(self) -> None:
        self.stack.pop()
        return
        

    def top(self) -> int:
        return self.stack[-1][1]

    def getMin(self) -> int:
        return self.stack[-1][0]
