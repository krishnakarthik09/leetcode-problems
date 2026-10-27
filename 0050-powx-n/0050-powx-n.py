class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1.00000
        flag=False
        if n<0:
            flag=True
            n*=-1
        while n>0:
            if n%2==0:
                x=x*x
                n=n//2
            else:
                ans=ans*x
                n=n-1
        if flag:
            return 1.00000/ans
        return ans





        