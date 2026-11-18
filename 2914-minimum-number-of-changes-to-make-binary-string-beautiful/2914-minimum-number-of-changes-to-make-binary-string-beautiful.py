class Solution:
    def minChanges(self, s: str) -> int:
        count=0
        a=0
        b=0
        n=len(s)
        for i in range(n):
            if s[i]=="1":
                a+=1
            elif s[i]=="0":
                b+=1
            if (i+1)%2==0:
                if a==1 and b==1:
                    count+=1
                a=0
                b=0
        return count
            
             

        