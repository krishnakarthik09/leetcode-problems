class Solution:
    def reverseWords(self, s: str) -> str:
        res=""
        n=len(s)
        i=0
        j=n-1
        while i<j and s[j]==" ":
            j-=1
        while i<j and s[i]==" ":
            i+=1
        temp=""
        for k in range(j ,i-1,-1):
            if s[k]!=" ":
                temp+=s[k]
            else:
                res+=temp[::-1]
                if res[len(res)-1]!=" ":
                    res+=" "
                temp=""
        res=res+temp[::-1]
        return res