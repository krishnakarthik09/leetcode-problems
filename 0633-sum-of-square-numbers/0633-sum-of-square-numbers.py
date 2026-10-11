class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n=int(c**(0.5))
        i=0
        while i<=n:
            total=(i*i)+(n*n)
            if total==c:
                return True
            elif total>c:
                n-=1
            else:
                i+=1
        return False

        