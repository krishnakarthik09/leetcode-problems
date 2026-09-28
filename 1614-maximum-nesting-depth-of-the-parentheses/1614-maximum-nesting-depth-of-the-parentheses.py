class Solution:
    def maxDepth(self, s: str) -> int:
        n=len(s)
        depth=0
        maxdepth=0
        for i in range(n):
            if s[i]=="(":
                depth+=1
                maxdepth=max(maxdepth,depth)
            elif s[i]==")":
                depth-=1
        return maxdepth
            
        