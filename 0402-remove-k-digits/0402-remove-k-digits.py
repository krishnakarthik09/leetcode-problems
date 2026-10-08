class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        n=len(num)
        if n==k:
            return "0"
            
        for i in range(n):
            while st and k>0 and int(st[-1])>int(num[i]):
                st.pop()
                k-=1
            st.append(num[i])
        if k>0 and st:
            while st and k>0:
                st.pop()
                k-=1
        ans=""
        for d in st:
            if len(ans)==0 and int(d)==0:
                continue
            else:
                ans+=d
        if ans=="":
            return "0"
        return ans
        
        