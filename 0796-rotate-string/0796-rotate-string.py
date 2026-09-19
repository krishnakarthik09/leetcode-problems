class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        n=len(s)
        m=len(goal)
        for start in range(len(goal)):
            i=0
            while i<n:
                if s[i]!=goal[(start+i)%m]:
                    break
                i+=1
            if i>=n:
                return True
        return False
                

