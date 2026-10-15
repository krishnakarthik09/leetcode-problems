class StockSpanner:

    def __init__(self):
        self.st=[]
        self.ind=-1
        

    def next(self, price: int) -> int:
        while self.st and self.st[-1][0]<=price:
            self.st.pop()
        if self.st:
            top=self.st[-1][1]
        else:
            top=-1
        self.st.append([price,self.ind+1])
        self.ind+=1

        return self.st[-1][1]-top
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)