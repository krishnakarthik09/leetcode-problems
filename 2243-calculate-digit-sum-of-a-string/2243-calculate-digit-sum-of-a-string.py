class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            ans=[]
            groupsum=0
            r=k
            for i in range(len(s)):
                if r>0:
                    groupsum+=int(s[i])
                    r-=1
                else:
                    ans.append(str(groupsum))
                    groupsum=int(s[i])
                    r=k-1
    
            ans.append(str(groupsum))
            s="".join(ans)
        return s


        