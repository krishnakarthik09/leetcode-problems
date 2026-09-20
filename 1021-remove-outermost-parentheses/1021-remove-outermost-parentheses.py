class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth=0
        res=""
        n=len(s)
        for i in range(0,n):
            if s[i]=='(':
                depth+=1
                if depth>1:
                    res+=s[i]
            if  s[i]==')':
                depth-=1
                if depth>=1:
                    res+=s[i]
        return res
        