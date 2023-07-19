class MinStack:

    def __init__(self):
        self.item = []
        self.minVal = []
        

    def push(self, val: int) -> None:
        self.item.append(val)
        val = min(self.minVal[-1] if self.minVal else val, val)
        self.minVal.append(val)
        

    def pop(self) -> None:
        if self.item:
            self.item.pop()
            self.minVal.pop()

        

    def top(self) -> int:
        if self.item:
            return self.item[-1]
            
        

    def getMin(self) -> int:
        if self.minVal:
            return self.minVal[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
