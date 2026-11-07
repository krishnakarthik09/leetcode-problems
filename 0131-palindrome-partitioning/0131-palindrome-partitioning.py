class Solution:
    def ispalindrome(self,s , left,right):
        while left< right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    def solve(self,ind,s,subset,result):
        if ind>=len(s):
            result.append(subset.copy())
            return
        for i in range(ind,len(s)):
            if self.ispalindrome(s,ind,i):
                subset.append(s[ind:i+1])
                self.solve(i+1,s,subset,result)
                subset.pop()
    def partition(self, s: str) -> list[list[str]]:
        result=[]
        self.solve(0,s,[],result)
        return result
        