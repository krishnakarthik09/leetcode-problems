class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        res=""
        for i in range(0,n):
            left=i
            right=i
            while left>=0 and right<n:
                if s[left]!=s[right]:
                    break
                if len(res)<(right-left+1):
                    res=s[left:right+1]
                left-=1
                right+=1
            right=i+1
            left=i
            while left>=0 and right<n:
                if s[left]!=s[right]:
                    break
                if len(res)<(right-left+1):
                    res=s[left:right+1]
                left-=1
                right+=1
        return res
            