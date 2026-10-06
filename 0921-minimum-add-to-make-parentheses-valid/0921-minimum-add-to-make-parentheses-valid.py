class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        n=len(s)
        rem=0
        for i in range(0,n):
            if s[i]=='(':
                st.append(s[i])
            else:
                if st:
                    st.pop()
                else:
                    rem+=1
        return rem+len(st)


        