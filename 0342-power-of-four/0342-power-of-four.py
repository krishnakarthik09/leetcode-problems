class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        if n&(n-1)==0 and n>0:
            count=0
            while n>1:
                count+=1
                n=n//2
            if count%2==0:
                return True
        return False
        