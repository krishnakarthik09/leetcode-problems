class Solution:
    def expand(self, s, left, right):
        n=len(s)
        count=0
        while left>=0 and right<n and s[left]==s[right]:
            count+=1
            left-=1
            right+=1
        return count
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        count=0
        for i in range(n):
            count+=self.expand(s,i,i)
            count+=self.expand(s,i,i+1)
        return count
    

        