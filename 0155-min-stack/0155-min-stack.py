class MinStack:

    def __init__(self):
        self.items=[]
        self.ministack=[]
        self.mini=float("inf")
        

    def push(self, value: int) -> None:
        if value<=self.mini:
            self.mini=value
            self.ministack.append(value)
        self.items.append(value)
        return 
        

    def pop(self) -> None:
        if len(self.items)!=0:
            if self.items[-1]==self.mini:
                self.ministack.pop()
                if len(self.ministack)==0:
                    self.mini=float("inf")
                else:
                    self.mini=self.ministack[-1]
            self.items.pop()
        return
        

    def top(self) -> int:
        if len(self.items)!=0:
            x=self.items[-1]
            return x
        

    def getMin(self) -> int:
        return self.mini
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()