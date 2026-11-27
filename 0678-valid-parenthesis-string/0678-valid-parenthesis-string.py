class Solution:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        mini=0
        maxi=0
        for i in range(n):
            if s[i]=='(':
                mini+=1
                maxi+=1
            elif s[i]=='*':
                mini=max(mini-1,0)
                maxi+=1
            else:
                mini=max(mini-1,0)
                maxi-=1
                if maxi<0:
                    return False
                
            
        return mini==0
        