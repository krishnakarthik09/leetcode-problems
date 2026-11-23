class ProductOfNumbers:

    def __init__(self):
        self.stream=[]
        self.product=1
        self.length=0
        self.last=-1
        

    def add(self, num: int) -> None:
        if num!=0:
            self.product*=num
        else:
            self.last=self.length
        self.stream.append(self.product)
        self.length+=1
        

    def getProduct(self, k: int) -> int:
        n=self.length
        if k>n:
            return 0
        if n-k<=self.last<=n:
            return 0
        if k==n:
            return self.stream[-1]
        return self.stream[-1]//self.stream[n-k-1]
        # ans=1
        # for i in range(n-1,n-k-1,-1):
        #     ans*=self.stream[i]
       
        # return ans
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)